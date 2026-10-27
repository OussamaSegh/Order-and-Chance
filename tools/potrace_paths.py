"""Small ctypes bridge to the system Potrace library, used only by art generation.

Potrace traces sampled boundaries into cubic Bezier curves. The generated print
assets contain paths, not enlarged pixels. Install libpotrace0 to regenerate them.
"""
import ctypes as c
import ctypes.util

import numpy as np


class Point(c.Structure):
    _fields_ = [('x', c.c_double), ('y', c.c_double)]


class Curve(c.Structure):
    _fields_ = [('n', c.c_int), ('tag', c.POINTER(c.c_int)),
                ('c', c.POINTER(Point * 3))]


class Path(c.Structure):
    pass


Path._fields_ = [('area', c.c_int), ('sign', c.c_int), ('curve', Curve),
                 ('next', c.POINTER(Path)), ('childlist', c.POINTER(Path)),
                 ('sibling', c.POINTER(Path)), ('priv', c.c_void_p)]


class State(c.Structure):
    _fields_ = [('status', c.c_int), ('plist', c.POINTER(Path)), ('priv', c.c_void_p)]


class Progress(c.Structure):
    _fields_ = [('callback', c.c_void_p), ('data', c.c_void_p),
                ('min', c.c_double), ('max', c.c_double), ('epsilon', c.c_double)]


class Param(c.Structure):
    _fields_ = [('turdsize', c.c_int), ('turnpolicy', c.c_int),
                ('alphamax', c.c_double), ('opticurve', c.c_int),
                ('opttolerance', c.c_double), ('progress', Progress)]


class Bitmap(c.Structure):
    _fields_ = [('w', c.c_int), ('h', c.c_int), ('dy', c.c_int),
                ('map', c.POINTER(c.c_ulong))]


def trace(mask, tolerance=.2, speckle=0):
    """Return one SVG path, including holes, from a boolean foreground mask."""
    libname = ctypes.util.find_library('potrace')
    if not libname:
        raise RuntimeError('Install libpotrace0 before regenerating print artwork')
    lib = c.CDLL(libname)
    lib.potrace_param_default.restype = c.POINTER(Param)
    lib.potrace_param_free.argtypes = [c.POINTER(Param)]
    lib.potrace_trace.argtypes = [c.POINTER(Param), c.POINTER(Bitmap)]
    lib.potrace_trace.restype = c.POINTER(State)
    lib.potrace_state_free.argtypes = [c.POINTER(State)]
    h, w = mask.shape
    bits = c.sizeof(c.c_ulong) * 8
    dy = (w + bits - 1) // bits
    padded = np.pad(mask, ((0, 0), (0, dy * bits - w)))
    packed = np.packbits(padded, axis=1, bitorder='big').tobytes()
    words = np.frombuffer(packed, dtype=f'>u{bits // 8}').astype(
        np.uint64 if bits == 64 else np.uint32)
    bitmap = Bitmap(w, h, dy, words.ctypes.data_as(c.POINTER(c.c_ulong)))
    param = lib.potrace_param_default()
    if not param:
        raise MemoryError('Could not allocate Potrace parameters')
    param.contents.turdsize = speckle
    param.contents.alphamax = 1.0
    param.contents.opttolerance = tolerance
    state = lib.potrace_trace(param, c.byref(bitmap))
    result = []
    try:
        if not state or state.contents.status:
            raise RuntimeError('Potrace did not finish the contour trace')
        node = state.contents.plist
        while node:
            curve = node.contents.curve
            start = curve.c[curve.n - 1][2]
            path = [f'M{start.x:.3f},{start.y:.3f}']
            for i in range(curve.n):
                points = curve.c[i]
                if curve.tag[i] == 2:
                    path.append(f'L{points[1].x:.3f},{points[1].y:.3f} '
                                f'{points[2].x:.3f},{points[2].y:.3f}')
                else:
                    path.append('C' + ' '.join(f'{q.x:.3f},{q.y:.3f}' for q in points))
            path.append('Z')
            result.append(' '.join(path))
            node = node.contents.next
        return ' '.join(result)
    finally:
        if state:
            lib.potrace_state_free(state)
        lib.potrace_param_free(param)
