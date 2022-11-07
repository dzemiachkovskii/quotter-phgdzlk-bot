from PIL import Image, ImageFont, ImageDraw
import config


def getimg(quote: list, customimg=None):
    img = Image.open(config.TEMPLATE)
    if customimg is not None:
        img = customimg

    quote[2] = '© ' + quote[2]

    font_text = ImageFont.truetype(config.LOBSTER, size=18)
    font_author = ImageFont.truetype(config.LOBSTER, size=22)

    im_w, im_h = img.size

    font_text_w, font_text_h = font_text.getsize(quote[1])
    font_author_w, font_author_h = font_author.getsize(quote[2])

    ft_new_w = (im_w - font_text_w) / 6
    ft_new_h = (im_h - font_text_h) / 2 + (im_h - font_author_h) / 4
    fa_new_w = (im_w - font_author_w) / 6
    fa_new_h = (im_h - font_author_h) / 2 + (im_h - font_author_h) / 2.3

    draw = ImageDraw.Draw(img)
    draw.text(xy=(ft_new_w, ft_new_h), text=quote[1], fill='#ffffff', font=font_text)
    draw.text(xy=(fa_new_w, fa_new_h), text=quote[2], fill='#ffffff', font=font_author)

    return img
