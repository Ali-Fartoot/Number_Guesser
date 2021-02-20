from PaintAPP import init, return_resume
from ScalingDataTest import resize_image

# initialize "MYPaintApp"
init()
if return_resume():
    # resize image to 28 X 28 pixel
    resize_image()