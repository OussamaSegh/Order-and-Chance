"""Vector scene in model units -> TikZ in cover inches, fitted between the rules and centred by visual mass."""
import math, numpy as np
BOX=(0.62,5.38,3.20,6.66)     # x0,x1,y0,y1 inches (between the fixed rules)
CX,CY=3.0,(BOX[2]+BOX[3])/2
def rdp(S,tol):
    if len(S)<3: return np.arange(len(S))
    keep=np.zeros(len(S),bool); keep[0]=keep[-1]=True; st=[(0,len(S)-1)]
    while st:
        a,b=st.pop()
        if b<=a+1: continue
        A,B=S[a],S[b]; d=B-A; n=math.hypot(*d); seg=S[a+1:b]-A
        dist=np.abs(seg[:,0]*d[1]-seg[:,1]*d[0])/n if n>1e-12 else np.hypot(seg[:,0],seg[:,1])
        k=int(np.argmax(dist))
        if dist[k]>tol: m=a+1+k; keep[m]=True; st+=[(a,m),(m,b)]
    return np.nonzero(keep)[0]
class Scene:
    def __init__(s): s.items=[]
    def line(s,pts,w=0.6,op=1.0,col='ocCoral',glow=0.0,cap='round'):
        P=np.asarray(pts,float)
        if len(P)>1: s.items.append(('line',P,w,op,col,glow))
    def dot(s,x,y,r,col='ocCoral',op=1.0,halo=0.0,scaled=True):
        s.items.append(('dot',np.array([[x,y]],float),r,op,col,halo,scaled))
    def fill(s,pts,col='ocCoral',op=0.1):
        s.items.append(('fill',np.asarray(pts,float),col,op))
    def circle(s,x,y,r,w=0.5,op=1,col='ocCoral',glow=0.0):
        s.items.append(('circle',np.array([[x,y]],float),r,w,op,col,glow))
    def arc(s,x,y,r,a0,a1,w=0.5,op=1,col='ocCoral',glow=0.0):   # degrees, counter-clockwise a0->a1
        s.items.append(('arc',np.array([[x,y]],float),r,a0,a1,w,op,col,glow))
    # ---------- geometry ----------
    def bounds(s):
        lo=np.array([np.inf,np.inf]); hi=-lo
        for it in s.items:
            k=it[0]; P=it[1]
            if k in ('line','fill'): lo=np.minimum(lo,P.min(0)); hi=np.maximum(hi,P.max(0))
            elif k=='dot': r=it[2] if it[6] else 0; lo=np.minimum(lo,P[0]-r); hi=np.maximum(hi,P[0]+r)
            elif k=='circle': lo=np.minimum(lo,P[0]-it[2]); hi=np.maximum(hi,P[0]+it[2])
            elif k=='arc':
                t=np.radians(np.linspace(it[3],it[4],64)); Q=P[0]+it[2]*np.stack([np.cos(t),np.sin(t)],1)
                lo=np.minimum(lo,Q.min(0)); hi=np.maximum(hi,Q.max(0))
        return lo,hi
    def mass_x(s):
        num=den=0.0
        for it in s.items:
            k=it[0]
            if k=='line':
                P=it[1]; L=np.hypot(*np.diff(P,axis=0).T); m=(P[1:,0]+P[:-1,0])/2; w=it[2]*it[3]*(1+it[5])
                num+=(L*m).sum()*w; den+=L.sum()*w
            elif k=='dot':
                w=it[3]*(it[2] if it[6] else 0.01)*6*(1+it[5]); num+=it[1][0,0]*w; den+=w
            elif k=='circle':
                w=2*math.pi*it[2]*it[3]*it[4]*(1+it[6]); num+=it[1][0,0]*w; den+=w
            elif k=='arc':
                t=np.radians(np.linspace(it[3],it[4],33)); x=it[1][0,0]+it[2]*np.cos(t)
                L=abs(math.radians(it[4]-it[3]))*it[2]; w=it[5]*it[6]*(1+it[8]); num+=x.mean()*L*w; den+=L*w
        return num/den
    def to_tikz(s,center='mass',fill_frac=1.0,box=BOX):
        lo,hi=s.bounds(); bw,bh=box[1]-box[0],box[3]-box[2]
        k=min(bw/(hi[0]-lo[0]),bh/(hi[1]-lo[1]))*fill_frac
        ycen=(box[2]+box[3])/2
        if center in('mass','avg'):
            mx=s.mass_x() if center=='mass' else (s.mass_x()+(lo[0]+hi[0])/2)/2; ox=CX-k*mx
            # keep the bounding box inside the art area
            ox=min(max(ox,box[0]-k*lo[0]),box[1]-k*hi[0])
        else: ox=CX-k*(lo[0]+hi[0])/2
        oy=ycen-k*(lo[1]+hi[1])/2
        T=lambda P:np.stack([ox+k*P[:,0],oy+k*P[:,1]],1)
        s.k,s.ox,s.oy=k,ox,oy
        fmt=lambda P:'--'.join('(%.4fin,%.4fin)'%(x,y) for x,y in P)
        out=[]; groups={}; halos={}
        for it in s.items:
            kind=it[0]
            if kind=='fill':
                out.append(r'\fill[%s,opacity=%.3f] %s--cycle;'%(it[2],it[3],fmt(T(it[1]))))
        for it in s.items:
            kind=it[0]
            if kind=='line':
                _,P,w,op,col,glow=it; Q=T(P); Q=Q[rdp(Q,0.0012)]
                groups.setdefault((col,round(w,3),round(op,3)),[]).append(fmt(Q))
                if glow>0: halos.setdefault(('ocCoverCoral' if col!='ocCoverTitle' else 'ocCoverTitle',round(w,3),round(glow,2)),[]).append(fmt(Q))
            elif kind=='circle':
                _,P,r,w,op,col,glow=it; Q=T(P)[0]; d='(%.4fin,%.4fin) circle (%.5fin)'%(Q[0],Q[1],r*k)
                groups.setdefault((col,round(w,3),round(op,3)),[]).append(d)
                if glow>0: halos.setdefault(('ocCoverCoral',round(w,3),round(glow,2)),[]).append(d)
            elif kind=='arc':
                _,P,r,a0,a1,w,op,col,glow=it; c=T(P)[0]
                d='(%.4fin,%.4fin) arc[start angle=%.4f,end angle=%.4f,radius=%.5fin]'%(c[0]+r*k*math.cos(math.radians(a0)),c[1]+r*k*math.sin(math.radians(a0)),a0,a1,r*k)
                groups.setdefault((col,round(w,3),round(op,3)),[]).append(d)
                if glow>0: halos.setdefault(('ocCoverCoral',round(w,3),round(glow,2)),[]).append(d)
        def batch(opts,paths,n=150):
            return [r'\draw[%s,line cap=round,line join=round] %s;'%(opts,' '.join(paths[i:i+n])) for i in range(0,len(paths),n)]
        for (col,w,g),paths in halos.items():
            out+=batch('draw=%s,line width=%.2fpt,draw opacity=%.4f'%(col,w*6,0.06*g),paths)
            out+=batch('draw=%s,line width=%.2fpt,draw opacity=%.4f'%(col,w*2.6,0.16*g),paths)
        for (col,w,op),paths in groups.items():
            out+=batch('draw=%s,line width=%.3fpt,draw opacity=%.3f'%(col,w,op),paths)
        for it in s.items:
            if it[0]=='dot':
                _,P,r,op,col,halo,scaled=it; Q=T(P)[0]; rr=r*k if scaled else r
                if halo>0: out.append(r'\fill[ocCoral,opacity=%.3f] (%.4fin,%.4fin) circle (%.5fin);'%(0.18*halo,Q[0],Q[1],rr*2.4))
                out.append(r'\fill[%s,opacity=%.3f] (%.4fin,%.4fin) circle (%.5fin);'%(col,op,Q[0],Q[1],rr))
        return out
