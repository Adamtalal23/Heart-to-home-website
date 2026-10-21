import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageDraw
U="/root/.claude/uploads/48e229c6-43cb-57ad-9f72-daf0ca6a5f5a/81f196c7-image.jpg"
CHK="/tmp/claude-0/-home-claude/48e229c6-43cb-57ad-9f72-daf0ca6a5f5a/scratchpad/"
OUT="/home/claude/h2h/site/images/"
im=ImageOps.exif_transpose(Image.open(U)).convert("RGB"); im.thumbnail((1400,1400))
a=np.asarray(im).astype(float); H,W,_=a.shape
L=a.mean(2); mx=a.max(2); mn=a.min(2); sat=(mx-mn)/(mx+1)
P=Image.new("L",(W,H),0); d=ImageDraw.Draw(P)
d.polygon([(726,141),(940,167),(906,545),(702,507),(712,300),(722,190),(740,177)],fill=255)   # back wall
d.polygon([(940,167),(1050,159),(1050,568),(906,545)],fill=255)                               # right wall
d.polygon([(285,97),(726,141),(740,177),(600,170),(285,138)],fill=255)                         # strip above uppers
d.polygon([(701,232),(894,242),(870,449),(699,468)],fill=0)                                      # window out
P=np.asarray(P)>0
R=Image.new("L",(W,H),0); ImageDraw.Draw(R).polygon([(940,167),(1050,159),(1050,568),(906,545)],fill=255); R=np.asarray(R)>0
keep=(P&(sat<0.22)&(L>95))|(R&(L>95))
m=Image.fromarray((keep*255).astype("uint8")).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(1))
m.save(OUT+"wall-mask.png"); im.save(OUT+"wall-room.jpg",quality=85,optimize=True)
mm=np.asarray(m).astype(float)/255; Lm=L[keep].mean(); print("meanL",Lm, keep.mean())
tiles=[]
for t in [(47,61,76),(149,151,138),(172,107,83)]:
    f=np.clip((L/Lm)**0.8,0.5,1.45)[...,None]*np.array(t,float)
    out=a*(1-mm[...,None])+np.clip(f,0,255)*mm[...,None]
    o=Image.fromarray(out.astype("uint8")); o.thumbnail((500,700)); tiles.append(o)
s=Image.new("RGB",(sum(t.width for t in tiles)+20,tiles[0].height),"white"); x=0
for t in tiles: s.paste(t,(x,0)); x+=t.width+10
s.save(CHK+"kit.jpg")
