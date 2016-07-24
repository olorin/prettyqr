prettyqr
========

Create QR codes merged with images.

Example usage
-------------

Take a background image:

![Original image](img/dna-orig.png)

And a URL or some other text:

```
foo.com
```

Combine them:

```
prettyqr foo.com img/dna-orig.png --outfile img/dna-qr.png
```

![QR code image](img/dna-qr.png)

Command-line options
--------------------

```
usage: prettyqr [-h] [--border BORDER] [--out-file OUT_FILE]
                [--qr-opacity QR_OPACITY] [--qr-red QR_RED]
                [--qr-green QR_GREEN] [--qr-blue QR_BLUE]
                DATA IMAGE-FILE

Make pretty QR codes.

positional arguments:
  DATA                  Data to encode (e.g., "http://example.com").
  IMAGE-FILE            Image file to composite (e.g., "lena.jpg").

optional arguments:
  -h, --help            show this help message and exit
  --border BORDER       Size of border (in multiples of QR module size).
                        Defaults to 4. Can be zero if the QR code is intended
                        for printing or use on a light background.
  --out-file OUT_FILE   Path to write composite image file to. Extension will
                        determine the output format. Defaults to
                        "prettyqr.png".
  --qr-opacity QR_OPACITY
                        Opacity of the QR code modules, between 0 (invisible)
                        and 255 (opaque). Default is 200.
  --qr-red QR_RED       Red element of the QR module color, between 0 and 255.
                        Default is 0.
  --qr-green QR_GREEN   Green element of the QR module color, between 0 and
                        255. Default is 0.
  --qr-blue QR_BLUE     Blue element of the QR module color, between 0 and
                        255. Default is 0.
```

Limitations
-----------

`prettyqr` is a fairly raw proof-of-concept, and currently has an
assortment of limitations:

 - Only supports square images.
 - Only supports square QR modules.
 - Doesn't support complex color changes in the source image.

It will work best with sources where the focus of the image is not
central, and doesn't handle black backgrounds very well.

All of these issues are fairly tractable; patches are welcome.
