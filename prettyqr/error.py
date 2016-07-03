class PrettyException(Exception):
    "Semantic errors in prettyqr."
    pass

class ImageNotSquareException(PrettyException):
    pass

class BaseImageSmallerThanQRCodeException(PrettyException):
    pass
