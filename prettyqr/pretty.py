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

def make_pretty_qr(data, img, border=4, box_size=10, out_path="qr.png"):
    base_img = load_image(img)
    base_img_size = base_img.size[0]

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=0, # we make our own border
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image()

    border_px = border * box_size
    qr_w = base_img_size - (border_px * 2)
    qr_h = base_img_size - (border_px * 2)

    qr_scaled = qr_img.resize((qr_w, qr_h))

    qr_box = (
        border_px,
        border_px,
        base_img_size - border_px,
        base_img_size - border_px
    )
    base_img.paste(qr_scaled, qr_box)

    base_img.save(out_path)
    
