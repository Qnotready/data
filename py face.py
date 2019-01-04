#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
img = Image.open(".\\pictures\\zhongzhi.jpg")
#jgz = Image.open(".\\face1.png")
#img.paste(jgz, (195, 140))
draw=ImageDraw.Draw(img)
ttfront=ImageFont.truetype('simhei.ttf',25)
draw.text((12,250),"兰强：看到这根指头没有？！\n下一秒就会插到你的身上！",fill=(0,0,0),font=ttfront)
img.show()
img.save(".\\pictures\\picture4.jpg")