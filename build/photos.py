import sys
from PIL import Image, ImageFilter, ImageOps
U = "/root/.claude/uploads/48e229c6-43cb-57ad-9f72-daf0ca6a5f5a/"
OUT = "/home/claude/h2h/site/images/"
CHK = "/tmp/claude-0/-home-claude/48e229c6-43cb-57ad-9f72-daf0ca6a5f5a/scratchpad/chk/"
P = [  # src, out name, blur boxes (actual px)
 ("49cdcb95", "kitchen-a-before-1.jpg", []),
 ("6e815cbf", "kitchen-a-before-2.jpg", []),
 ("d8fd3f7b", "kitchen-b-after-1.jpg", []),
 ("3c706be1", "kitchen-b-after-2.jpg", []),
 ("e8370525", "exterior-a-before.jpg", []),
 ("bed69b2a", "exterior-a-progress.jpg", []),
 ("a9647caa", "exterior-a-after-1.jpg", [(1420, 910, 1600, 1000)]),
 ("6f1796c5", "exterior-a-after-2.jpg", [(2280, 1035, 2390, 1110)]),
 ("8d4f28b3", "exterior-b-before.jpg", []),
 ("764591e2", "exterior-b-after.jpg", []),
 ("72426976", "interior-accent-wall.jpg", []),
 ("298c775b", "fireplace-wall-framing.jpg", [(195, 750, 935, 1170)]),
 ("bff5acd7", "fireplace-wall-finished.jpg", [(245, 730, 940, 1140)]),
 ("c84a78bb", "flooring-before.jpg", []),
 ("eb40c655", "flooring-after.jpg", []),
]
for src, name, boxes in P:
    im = ImageOps.exif_transpose(Image.open(U + src + "-image.jpg")).convert("RGB")
    for b in boxes:
        reg = im.crop(b).filter(ImageFilter.GaussianBlur(28))
        im.paste(reg, b)
        im.crop((max(0,b[0]-150), max(0,b[1]-150), min(im.width,b[2]+150), min(im.height,b[3]+150))).save(CHK + name)
    im.thumbnail((1600, 1600))
    im.save(OUT + name, "JPEG", quality=80, optimize=True, progressive=True)  # no EXIF carried over
print("ok")
