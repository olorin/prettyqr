import sys

from .pretty import make_pretty_qr

def main():
    data = sys.argv[1]
    img = sys.argv[2]
    outfile = "prettyqr.png"
    if len(sys.argv) > 3:
        outfile = sys.argv[3]
    qr = make_pretty_qr(data, img)
    qr.save(outfile)
