from PIL import Image
import qrcode

from .error import *

def load_image(fname):
    im = Image.open(fname)
    (w, h) = im.size
    if w != h:
        raise ImageNotSquareException
    return im

def make_pretty_qr(data, img, out_path="qr.png"):
    backing_img = load_image(img)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image()
    qr_scaled = qr_img.resize(backing_img.size)
    qr_scaled.save(out_path)
    
