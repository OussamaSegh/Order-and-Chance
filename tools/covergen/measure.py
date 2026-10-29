"""Measure ink of ivory text lines and of the coral illustration on a rendered cover PNG."""
import sys, numpy as np
from PIL import Image
def measure(path,art_top_in=6.9,art_bot_in=2.95):
    im=np.asarray(Image.open(path).convert('RGB')).astype(int); H,W,_=im.shape
    ppi=W/6.0; cx=W/2
    R,G,B=im[...,0],im[...,1],im[...,2]
    ivory=(G>120)&(B>110)&(R>140)&(abs(R-G)<60)
    ivory[:, :int(0.33*ppi)]=False; ivory[:, W-int(0.33*ppi):]=False
    ivory[:int(0.33*ppi)]=False; ivory[H-int(0.33*ppi):]=False
    yt=int((8.5714-art_top_in)*ppi)-4; yb=int((8.5714-art_bot_in)*ppi)+4
    rows=ivory.any(1); rows[yt:yb]=False
    bands=[];y=0
    while y<H:
        if rows[y]:
            y0=y
            while y<H and (rows[y] or rows[min(H-1,y+1)] or rows[min(H-1,y+2)]): y+=1
            cols=np.nonzero(ivory[y0:y].any(0))[0]; bands.append((y0,y,cols.min(),cols.max(),(cols.min()+cols.max())/2-cx))
        y+=1
    coral=(R>120)&(R-G>50); coral[:yt+6]=False; coral[yb-6:]=False
    coral[:, :int(0.33*ppi)]=False; coral[:, W-int(0.33*ppi):]=False
    wgt=np.where(coral,R-21,0).astype(float); xs=np.arange(W)
    ccx=(wgt.sum(0)*xs).sum()/wgt.sum()-cx; cols=np.nonzero(coral.any(0))[0]
    return bands,dict(centroid_dx=ccx,bbox_dx=(cols.min()+cols.max())/2-cx,bbox=(int(cols.min()),int(cols.max())))
if __name__=='__main__':
    for p in sys.argv[1:]:
        b,a=measure(p); print(p); [print('  rows %4d-%4d  x %4d-%4d  centre dx %+.1f px'%t) for t in b]; print('  art',a)
