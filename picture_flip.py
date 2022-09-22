
from operator import invert
import os
from PIL import Image, ImageChops

# main directory of images
directory = "C:/Users/Kevin/Documents/ImageFlip/images" 

# new folder where images will be stored
new_folder = "C:/Users/Kevin/Documents/ImageFlip/converted_images"

# check directory to create a folder if it does not exist
# check_directory = os.path.isdir(directory)

# if not check_directory:
#     os.makedirs(directory)


for image in os.listdir(directory):
    # sort files found in directory 
    sorted(image)
    print(image)

    img = Image.open(os.path.join(directory, image))
    

    # Resize images to 100x100 (does not preserve aspect ratio)
    resized_img = img.resize((100,100))

    # Convert to black and white
    bw_img = resized_img.convert('1')

    # Invert colours 
    inverted_bw_img = ImageChops.invert(bw_img)  

    # Flip images vertically
    flipped_img = inverted_bw_img.transpose(Image.FLIP_TOP_BOTTOM)

    # Show images
    # flipped_img.show()

    # returns original name of file from directory
    base_filename = os.path.basename(image)

    # splits the base file name into two parts
    name, ext = os.path.splitext(base_filename)

    # final path with new file name concatenated 
    final_path = os.path.join(new_folder, name + "_preprocessed" + ext)

    # save processed images to new directory
    flipped_img.save(final_path)




    