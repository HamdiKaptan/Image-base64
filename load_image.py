import base64
from io import BytesIO
from PIL import Image


def get_logo_image():
    return Image.open(BytesIO(base64.b64decode(logo_b64())))
def get_green_light():
    return Image.open(BytesIO(base64.b64decode(green_b64())))
def get_red_light():
    return Image.open((BytesIO(base64.b64decode(red_b64()))))
def get_normal_light():
    return Image.open((BytesIO(base64.b64decode(normal_b64()))))

def logo_b64():
    return " "
def green_b64():
    return ""
def red_b64():
    return ""
def normal_b64():
    return "https://www.base64-image.de outpu"
