# coding=utf-8
from PIL import Image, ImageDraw, ImageFont

def process(line): #换行函数
    temp = line
    text = ""
    while temp:
        text = text + temp[:8] + "\n"
        temp = temp[8:]
    return text

txt_small = "亲爱的" + input('亲爱的<请输入祝福的人姓名>：\n') + "："
txt_big = input('祝：<请输入祝福的话：>\n')
txt_samll_2 = input('祝福发出人：\n')

text_big_do = process(txt_big)

font_img = Image.open(".//img.jpg")
draw = ImageDraw.Draw(font_img)

front_small = ImageFont.truetype('.//ziti.ttf', 50)
front_big = ImageFont.truetype('.//ziti.ttf', 80)
'''draw.text((左右, 上下), 内容 , rgb颜色, font=front_small)'''
draw.text((230, 110), txt_small, fill=(0, 0, 0), font=front_small)
draw.text((240, 165), text_big_do, fill=(0, 0, 0), font=front_big)
draw.text((630, 355), txt_samll_2, fill=(0, 0, 0), font=front_small)

font_img.save(".//out.jpg")