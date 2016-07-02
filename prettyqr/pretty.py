from PIL import Image
import qrcode

from .error import *

def load_image(fname):
    im = Image.open(fname)
    (w, h) = im.size
    if w != h:
        raise ImageNotSquareException
    im_ = im.convert("RGBA")
    return im_

# FIXME: slow
def rgba_search_replace(img, old, new):
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            px = img.getpixel((x, y))
            if px == old:
                img.putpixel((x, y), new)

def make_qr(data, box_size, border, width, height):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=0, # we make our own border
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image().convert("RGBA")
    rgba_search_replace(qr_img, (255, 255, 255, 255), (0, 0, 0, 0))
    scale = width / qr_img.size[0]
    border_px = int(border * box_size * scale)
    qr_w = width - (border_px * 2)
    qr_h = height - (border_px * 2)
    qr_scaled = qr_img.resize((qr_w, qr_h))
    qr_layer = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
    qr_box = (
        border_px,
        border_px,
        height - border_px,
        width - border_px
    )
    qr_layer.paste(qr_scaled, qr_box)
    return qr_layer

def make_pretty_qr(data, img, border=4, out_path="qr.png"):
    base_img = load_image(img)
    qr_img = make_qr(data, 1, border, base_img.size[0], base_img.size[1])
    final_img = Image.alpha_composite(base_img, qr_img)

    final_img.save(out_path)
    
