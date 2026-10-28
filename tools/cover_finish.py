"""Give native mathematical plates the approved covers' luminous coral material.

Only rendering options change: every coordinate, formula, datum and path stays
intact. Nested vector strokes produce the halo without raster blur or filters.
"""
import re


def luminous_plate(source):
    def finish(match):
        command, options, geometry = match.groups()
        secondary = 'ocInk' in options
        width_match = re.search(r'line width=([.\d]+)pt', options)
        width = max(.42, float(width_match[1]) if width_match else .55)
        opacity_match = re.search(r'(?<![\w ])opacity=([.\d]+)', options)
        opacity = float(opacity_match[1]) if opacity_match else 1.
        fill_match = re.search(r'fill opacity=([.\d]+)', options)
        strength = float(fill_match[1]) if fill_match else opacity
        point = command == 'fill' and 'circle' in geometry
        tiny = 'circle' in geometry and width < .6
        outer = width + (2.8 if tiny else 6.0)
        middle = width + (1.4 if tiny else 3.0)
        inner = width + (.65 if tiny else 1.25)
        # Explicitly clear fill and arrowheads in the halo, retaining the path.
        halo = (f'preaction={{draw=ocCoverEmber,line width={outer:.3f}pt,'
                f'draw opacity={.06 if tiny else .09},fill opacity=0,arrows=-}},'
                f'preaction={{draw=ocCoverEmber,line width={middle:.3f}pt,'
                'draw opacity=.16,fill opacity=0,arrows=-},'
                f'preaction={{draw=ocCoverCoral,line width={inner:.3f}pt,'
                'draw opacity=.48,fill opacity=0,arrows=-}')
        options = re.sub(r'(?:^|,)(?:accent|ocInk|navy|draw=[^,]+|fill=[^,]+|'
                         r'line width=[^,]+|opacity=[^,]+|fill opacity=[^,]+)', '', options)
        options = options.strip(',')
        if command in ('fill', 'filldraw'):
            command = 'filldraw'
            material = (f'fill={"ocCoverPeak" if point else "ocCoverCoral"},'
                        f'fill opacity={.98 if point else .12+.22*strength:.3f},'
                        f'draw=ocCoverLight,draw opacity={.65+.35*strength:.3f},'
                        f'line width={.20 if point else .40:.3f}pt')
        else:
            material = (f'draw={"ocCoverCoral" if secondary else "ocCoverLight"},'
                        f'draw opacity={.48+.52*opacity:.3f},'
                        f'line width={width:.3f}pt')
            if not secondary and opacity >= .8 and width >= .65:
                material += (f',postaction={{draw=ocCoverPeak,line width={width*.28:.3f}pt,'
                             'draw opacity=.8,fill opacity=0,arrows=-}')
        return '\\' + command + '[' + ','.join(x for x in (options, halo, material) if x) + ']' + geometry

    return re.sub(r'\\(draw|filldraw|fill)\[([^\]]*)\]([^\n]*)', finish, source)
