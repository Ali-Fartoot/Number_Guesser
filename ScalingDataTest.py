# using Pillow module
from PIL import Image


def resize_image():
    try:
        # open
        img = Image.open('image.png')
        # resize file to 28 X 28 pixel
        img = img.resize((28, 28), Image.ANTIALIAS)
        # and save as "resized_image.png"
        img.save('resized_image.png')
    except IOError:
        print("cannot convert 'image.png'")
