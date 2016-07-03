import sys
import argparse

from .pretty import make_pretty_qr

def mkparser():
    parser = argparse.ArgumentParser(description="Make pretty QR codes.")
    parser.add_argument(
        "data",
        metavar="DATA",
        type=str,
        help="Data to encode (e.g., \"http://example.com\")."
    )
    parser.add_argument(
        "image",
        metavar="IMAGE-FILE",
        type=str,
        help="Image file to composite (e.g., \"lena.jpg\")."
    )
    parser.add_argument(
        "--border",
        dest="border",
        type=int,
        default=4,
        help="Size of border (in multiples of QR module size). Defaults to 4. Can be zero if the QR code is intended for printing or use on a light background."
    )
    parser.add_argument(
        "--out-file",
        dest="out_file",
        type=str,
        default="prettyqr.png",
        help="Path to write composite image file to. Extension will determine the output format. Defaults to \"prettyqr.png\"."
    )
    parser.add_argument(
        "--qr-opacity",
        dest="qr_opacity",
        type=int,
        default=200,
        help="Opacity of the QR code modules (black bits), between 0 (invisible) and 255 (opaque). Default is 200."
    )

    return parser

def main():
    args = mkparser().parse_args()
    qr = make_pretty_qr(
        args.data,
        args.image,
        border=args.border,
        black_opacity=args.qr_opacity,
    )
    qr.save(args.out_file)
