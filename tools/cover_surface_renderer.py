"""Render every world-space model with the same camera and fine coral material."""
import math
from series_cover import settings


def render(curves, data=None):
    data=settings() if data is None else data
    camera=data['camera'];origin=data['camera_origin_px'];material=data['material']
    project=lambda p:tuple(origin[i]+sum(camera[i][j]*p[j] for j in range(3)) for i in range(2))
    points=[p for curve in curves for p in curve]
    if not points or any(len(p)!=3 or not all(math.isfinite(v) for v in p) for p in points):
        raise ValueError('A cover illustration must be one finite world-space 3D model')
    ys=[project(p)[1] for p in points];lo,hi=min(ys),max(ys)
    scale=min(1.,data['art_height_px']/max(1.,hi-lo))
    mid=(lo+hi)/2
    def screen(p):
        x,y=project(p)
        return origin[0]+scale*(x-origin[0]),data['art_center_y_px']+scale*(y-mid)
    minz=min(p[2] for p in points);maxz=max(p[2] for p in points)
    crown=[screen(p) for p in points if p[2]>=maxz-.03*(maxz-minz)]
    focus=(sum(p[0] for p in crown)/len(crown),sum(p[1] for p in crown)/len(crown))
    commands=[];glows=[];segments=0
    # Fine contours and a local bloom at the crown, rather than uniform neon tubes.
    ordered=sorted(enumerate(curves),key=lambda item:sum(p[0]+p[1]+.606*p[2] for p in item[1])/len(item[1]))
    for index,curve in ordered:
        face=index in getattr(curves,'faces',set())
        pieces=[curve] if face else [curve[start:start+11] for start in range(0,len(curve)-1,10)]
        for segment in pieces:
            meanz=sum(p[2] for p in segment)/len(segment)
            z=(meanz+max(p[2] for p in segment))/2
            height=max(0.,min(1.,(z-minz)/(maxz-minz or 1)))
            xy=[screen(p) for p in segment];x=sum(p[0] for p in xy)/len(xy);y=sum(p[1] for p in xy)/len(xy)
            hot=max(0.,(height-.45)/.55)**1.8*math.exp(-((x-focus[0])/210)**2-((y-focus[1])/150)**2)
            rgb=[round((1-hot)*a+hot*b) for a,b in zip(material['coral'],material['highlight'])]
            color='{rgb,255:red,%d;green,%d;blue,%d}'%tuple(rgb)
            depth=max(0.,min(1.,(sum(p[0]+p[1] for p in segment)/len(segment)+2)/4))
            opacity=min(.99,(.55+.45*math.sqrt(height))*(.80+.20*depth)+.12*hot)
            width=material['line_width_pt']+(material['highlight_line_width_pt']-material['line_width_pt'])*hot
            options=f'draw={color},draw opacity={opacity:.3f},line width={width:.3f}pt,line cap=round,line join=round'
            path='--'.join(f'({x*6/1050:.5f}in,{(1500-y)*6/1050:.5f}in)' for x,y in xy)
            if face:
                # Opaque surface cells hide rear grid lines, as in the reference.
                commands.append('\\filldraw[fill=ocBlack,fill opacity=1,'+options+'] '+path+'--cycle;')
            else:commands.append('\\draw['+options+'] '+path+';')
            if hot>.15:
                halo=(f'draw={color},line width={width:.3f}pt,draw opacity={hot:.3f},'
                      f'preaction={{draw=ocCoverCoral,line width={material["glow_width_pt"]}pt,'
                      f'draw opacity={.18*hot:.3f}}},preaction={{draw=ocCoverLight,'
                      f'line width={material["glow_inner_width_pt"]}pt,draw opacity={.65*hot:.3f}}}')
                # Bloom is a final vector pass, so adjacent dark cells cannot erase it.
                glows.append('\\draw['+halo+'] '+path+';')
            segments+=1
    commands+=glows
    metadata={'space':'3D','world_curves':len(curves),'world_points':len(points),
              'opaque_surface_cells':len(getattr(curves,'faces',())),
              'rendered_segments':segments,'shared_camera':camera,'shared_material':material,
              'model_z_range':[minz,maxz],'uniform_fit_scale':scale}
    return '\n'.join(commands)+'\n',metadata
