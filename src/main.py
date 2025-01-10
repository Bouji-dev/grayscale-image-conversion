from PIL import Image
import numpy as np
"""
Converts a colorful image to grayscale using a weighted formula and saves the output.

The script reads an input image, converts it to grayscale using the formula:
    Y = 0.2126R + 0.7152G + 0.0722B
where R, G, and B are the red, green, and blue channels of the image, and Y is the resulting grayscale intensity.

Modules Used:
    - PIL (Python Imaging Library): For loading and saving images.
    - NumPy: For efficient numerical operations on the image array.

Steps:
    1. Load the original image from the specified `image_path`.
    2. Convert the image into a NumPy array for processing.
    3. Apply the grayscale conversion formula using matrix multiplication.
    4. Convert the resulting grayscale image data back to an image.
    5. Save the grayscale image to the specified `output_path`.

Variables:
    image_path (str): The path to the input colorful image (e.g., "colorful-image.jpeg").
    output_path (str): The path to save the output grayscale image (e.g., "grayscale-image.png").
    weights (list): The weights used for RGB to grayscale conversion.

Outputs:
    - Saves the grayscale image to the specified output path.

Notes:
    - The `image_data` shape is expected to be (height, width, 3), where the last dimension represents RGB channels.
    - The resulting grayscale image is saved as an 8-bit unsigned integer format.

Example:
    If the input image is colorful and has a shape of (168, 300, 3), the output grayscale image will have a shape of (168, 300).

Requirements:
    - Install PIL via `pip install pillow`.
    - Install NumPy via `pip install numpy`.
"""


image_path = "colorful-image.jpeg"
output_path = "grayscale-image.png"

original_image = Image.open(image_path)
image_data = np.asarray(original_image) 

# image_data.shape = (168, 300, 3)


# Y = (0.2126R + 0.7152G + 0.0722B)  the formula for converting to grayscale
weights = [0.2126 , 0.7152, 0.0722]
grayscale_image_data = image_data @ weights

grayscale_image_data = grayscale_image_data.astype('uint8')

grayscale_image = Image.fromarray(grayscale_image_data)
grayscale_image.save(output_path)