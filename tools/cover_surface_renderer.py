"""Hidden-line 3D geometry with soft, layered coral vector radiance.

The depth buffer only finds visible wires. Exported covers contain vector paths,
never a depth-buffer bitmap or a raster glow effect.
"""
import math
from collections import defaultdict
from series_cover import settings


def visible_edges(curves, screen, depth):
    """Remove rear wires before lighting, so halos cannot reveal hidden faces."""
    import numpy as np
    faces=getattr(curves,'faces',set())
    all_points=[screen(p) for curve in curves for p in curve]
    x0=math.floor(min(p[0] for p in all_points))-3
    y0=math.floor(min(p[1] for p in all_points))-3
    width=math.ceil(max(p[0] for p in all_points))-x0+4
    height=math.ceil(max(p[1] for p in all_points))-y0+4
    buffer=np.full((height,width),-np.inf)
    for index in faces:
        world=curves[index][:-1]
        if len(world)<3:continue
        center=tuple(sum(p[d] for p in world)/len(world) for d in range(3))
        for a,b in zip(world,world[1:]+world[:1]):
            tri=[(*screen(p),depth(p)) for p in (center,a,b)]
            (ax,ay,az),(bx,by,bz),(cx,cy,cz)=tri
            denominator=(by-cy)*(ax-cx)+(cx-bx)*(ay-cy)
            if abs(denominator)<1e-8:continue
            left=max(0,math.floor(min(ax,bx,cx))-x0);right=min(width-1,math.ceil(max(ax,bx,cx))-x0)
            top=max(0,math.floor(min(ay,by,cy))-y0);bottom=min(height-1,math.ceil(max(ay,by,cy))-y0)
            if left>right or top>bottom:continue
            xx,yy=np.meshgrid(np.arange(left,right+1)+x0,np.arange(top,bottom+1)+y0)
            aa=((by-cy)*(xx-cx)+(cx-bx)*(yy-cy))/denominator
            bb=((cy-ay)*(xx-cx)+(ax-cx)*(yy-cy))/denominator;cc=1-aa-bb
            inside=(aa>=-1e-8)&(bb>=-1e-8)&(cc>=-1e-8)
            tile=buffer[top:bottom+1,left:right+1]
            np.maximum(tile,np.where(inside,aa*az+bb*bz+cc*cz,-np.inf),out=tile)
    # Adjacent cells share wires. Emit each edge once, avoiding hot seams.
    edges={}
    for curve in curves:
        for a,b in zip(curve,curve[1:]):
            key=tuple(sorted(tuple(round(v,7) for v in p) for p in (a,b)))
            if key[0]!=key[1]:edges[key]=(a,b)
    visible=[]
    for a,b in edges.values():
        sa,sb=screen(a),screen(b)
        count=max(1,math.ceil(math.dist(sa,sb)/2));run=[]
        for k in range(count+1):
            t=k/count;p=tuple((1-t)*a[d]+t*b[d] for d in range(3));x,y=screen(p)
            ix=min(width-1,max(0,round(x)-x0));iy=min(height-1,max(0,round(y)-y0))
            nearest=float(buffer[iy,ix])
            shown=not math.isfinite(nearest) or depth(p)>=nearest-.025
            if shown:run.append(p)
            else:
                if len(run)>1:visible.append(run)
                run=[]
        if len(run)>1:visible.append(run)
    return visible,len(edges)


def render(curves, data=None, direction=None):
    data=settings() if data is None else data
    direction={} if direction is None else direction
    angles=[math.radians(a) for a in direction.get('rotation_deg',(0,0,0))]
    def rotate(p):
        x,y,z=p
        for axis,a in enumerate(angles):
            c,s=math.cos(a),math.sin(a)
            if axis==0:y,z=c*y-s*z,s*y+c*z
            elif axis==1:x,z=c*x+s*z,-s*x+c*z
            else:x,y=c*x-s*y,s*x+c*y
        return x,y,z
    from cover_surfaces import Scene
    curves=Scene([[rotate(p) for p in curve] for curve in curves],getattr(curves,'faces',()))
    camera=data['camera'];origin=data['camera_origin_px'];material=data['material']
    project=lambda p:tuple(origin[i]+sum(camera[i][j]*p[j] for j in range(3)) for i in range(2))
    points=[p for curve in curves for p in curve]
    if not points or any(len(p)!=3 or not all(math.isfinite(v) for v in p) for p in points):
        raise ValueError('A cover illustration must be one finite world-space 3D model')
    projected=[project(p) for p in points]
    ys=[p[1] for p in projected];lo,hi=min(ys),max(ys)
    xs=[p[0] for p in projected];left,right=min(xs),max(xs)
    clip=data['art_clip_px'];padding=12
    minimum_top=max(clip[1],direction.get('minimum_top_px',680))
    scale=min(direction.get('zoom',1.),(min(data['art_height_px'],clip[3]-minimum_top)-2*padding)/max(1.,hi-lo),
              (clip[2]-clip[0]-2*padding)/max(1.,right-left));mid=(lo+hi)/2
    target=direction.get('center_px',(660,data['art_center_y_px']))
    halfx=scale*(right-left)/2;halfy=scale*(hi-lo)/2
    centerx=max(clip[0]+padding+halfx,min(target[0],clip[2]-padding-halfx))
    centery=max(minimum_top+padding+halfy,min(target[1],clip[3]-padding-halfy))
    def screen(p):
        x,y=project(p)
        return centerx+scale*(x-(left+right)/2),centery+scale*(y-mid)
    normal=(camera[0][1]*camera[1][2]-camera[0][2]*camera[1][1],
            camera[0][2]*camera[1][0]-camera[0][0]*camera[1][2],
            camera[0][0]*camera[1][1]-camera[0][1]*camera[1][0])
    normal=tuple(v/max(abs(k) for k in normal) for v in normal)
    depth=lambda p:sum(a*b for a,b in zip(p,normal))
    edges,unique=visible_edges(curves,screen,depth)
    minz=min(p[2] for p in points);maxz=max(p[2] for p in points)
    groups=defaultdict(list)
    for segment in edges:
        z=sum(p[2] for p in segment)/len(segment)
        height=max(0.,min(1.,(z-minz)/(maxz-minz or 1)))
        band=round(height*20)
        xy=[screen(segment[0]),screen(segment[-1])]
        groups[band].append('--'.join(f'({x*6/1050:.5f}in,{(1500-y)*6/1050:.5f}in)' for x,y in xy))
    commands=['% Visible wires only; soft halo layers stay vector paths.']
    # Broad soft layers first, followed by narrower halos and sharp light cores.
    for width_factor,alpha in ((1.65,.025),(1.,.055),(.56,.12)):
        for band,paths in sorted(groups.items()):
            h=band/20;strength=.26+.74*h**1.7
            options=f'draw=ocCoverCoral,line width={material["glow_width_pt"]*width_factor:.3f}pt,draw opacity={alpha*strength:.4f}'
            commands.append('\\draw['+options+',line cap=round,line join=round] '+' '.join(paths)+';')
    for band,paths in sorted(groups.items()):
        h=band/20;hot=h**3;strength=.26+.74*h**1.7
        options=f'draw=ocCoverLight,line width={material["glow_inner_width_pt"]:.3f}pt,draw opacity={.33*strength:.4f}'
        commands.append('\\draw['+options+',line cap=round,line join=round] '+' '.join(paths)+';')
        rgb=[round((1-hot)*a+hot*b) for a,b in zip(material['coral'],material['highlight'])]
        color='{rgb,255:red,%d;green,%d;blue,%d}'%tuple(rgb)
        width=material['line_width_pt']+(material['highlight_line_width_pt']-material['line_width_pt'])*hot
        options=f'draw={color},line width={width:.3f}pt,draw opacity={.68+.32*math.sqrt(h):.4f}'
        commands.append('\\draw['+options+',line cap=round,line join=round] '+' '.join(paths)+';')
    metadata={'space':'3D','world_curves':len(curves),'world_points':len(points),
              'opaque_surface_cells':len(getattr(curves,'faces',())),
              'unique_world_edges':unique,'visible_wire_segments':len(edges),
              'rendered_segments':len(edges),'shared_camera':camera,'shared_material':material,
              'glow':'five-layer-vector-radiance','hidden_lines':'depth-tested-before-glow',
              'art_direction':direction,'screen_bounds_px':[centerx-halfx,centery-halfy,centerx+halfx,centery+halfy],
              'model_z_range':[minz,maxz],'uniform_fit_scale':scale}
    return '\n'.join(commands)+'\n',metadata
