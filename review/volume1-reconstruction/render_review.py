"""Render chapter samples and record actual PDF geometry/navigation."""
from pathlib import Path
import json,re
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'build/volume1-digital-review'
doc=fitz.open(ROOT/'dist/kdp/Volume 1 - The Integers - Print.pdf')
chapters=[(title,page) for level,title,page in doc.get_toc() if level==1]
samples=[]
for title,page in chapters:
    p=doc[page-1]
    pix=p.get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    samples.append((title,p.get_label(),im))
for first in range(0,len(samples),4):
    sheet=Image.new('RGB',(1240,1830),'#e3e3e3');draw=ImageDraw.Draw(sheet)
    for j,(title,label,im) in enumerate(samples[first:first+4]):
        im.thumbnail((600,860));x=10+(j%2)*620;y=35+(j//2)*910
        sheet.paste(im,(x,y));draw.text((x,y-22),title[:66]+' / '+label,fill='black')
    sheet.save(OUT/('chapters-'+str(first//4+1)+'.png'))
aux=(ROOT/'build/tome1-integers/main.aux').read_text()
keylabels=['prop:intcrit','prop:t1-norm-index','lem:cfexistence','prop:Zp','thm:henselnewton','thm:ostrowski']
for label in keylabels:
    m=re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{[^}]+\}\{([^}]+)\}',aux);assert m,label
    i=next(i for i,p in enumerate(doc) if p.get_label()==m[1])
    pix=doc[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False);pix.save(OUT/(label.replace(':','-')+'.png'))
reading=fitz.open(ROOT/'dist/Volume 1 - The Integers.pdf')
rects={(round(p.rect.width,3),round(p.rect.height,3)) for p in doc}
assert rects=={(504.0,720.0)},rects
assert len(reading)==len(doc)+1
assert len(chapters)==14,len(chapters)
links=sum(len(p.get_links()) for p in doc)
metrics=dict(interior_pages=len(doc),reading_pages=len(reading),last_printed_label=doc[-1].get_label(),page_sizes_pt=sorted(rects),chapter_bookmarks=len(chapters)-1,field_guide_bookmarks=1,internal_and_external_link_annotations=links,sampled_chapter_pages=[dict(title=t,label=l) for t,l,_ in samples],critical_sample_labels=keylabels)
(ROOT/'review/volume1-reconstruction/final-pdf-measurements.json').write_text(json.dumps(metrics,indent=2)+'\n')
print(json.dumps(metrics,indent=2))
