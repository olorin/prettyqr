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

def make_qr(data, box_size, border, width, height, black_opacity=200, white_opacity=25):
    qr = qrcode.QRCode(
        version=None, # pick version based on the data
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=0, # we make our own border
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image().convert("RGBA")
    rgba_search_replace(qr_img, (255, 255, 255, 255), (255, 255, 255, white_opacity))
    rgba_search_replace(qr_img, (0, 0, 0, 255), (0, 0, 0, black_opacity))
    scale = width / qr_img.size[0]
    border_px = int(border * box_size * scale)
    qr_w = width - (border_px * 2)
    qr_h = height - (border_px * 2)
    qr_scaled = qr_img.resize((qr_w, qr_h))
    qr_layer = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
    qr_box = (
        border_px, # from left
        border_px, # from top
        height - border_px, # from bottom
        width - border_px # from right
    )
    qr_layer.paste(qr_scaled, qr_box)
    return qr_layer

def make_pretty_qr(data, img, border=4):
    """
    Create an image from a QR encoding of the provided data, composited with
   the provided image file (which must be square) optimising for scannability.
    """
    base_img = load_image(img)
    qr_img = make_qr(data, 1, border, base_img.size[0], base_img.size[1])
    return Image.alpha_composite(base_img, qr_img)
    
