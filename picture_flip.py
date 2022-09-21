
from operator import invert
import os, PIL
from PIL import Image, ImageChops

directory = "C:/Users/Kevin/Downloads/ImageFlip/images"

new_folder = "C:/Users/Kevin/ImageFlip/converted_images"

# check directory to create a folder if it does not exist
# check_directory = os.path.isdir(directory)

# if not check_directory:
#     os.makedirs(directory)


for image in os.listdir(directory):

    img = Image.open(os.path.join(directory, image))

    # Resize images 
    resized_img = img.resize((100,100))

    # Convert to black and white
    bw_img = resized_img.convert('1')

    # Invert colours 
    inverted_bw_img = ImageChops.invert(bw_img)  

    # Flip images vertically
    flipped_img = inverted_bw_img.transpose(Image.FLIP_TOP_BOTTOM)

    # Show images
    flipped_img.show()

    



    