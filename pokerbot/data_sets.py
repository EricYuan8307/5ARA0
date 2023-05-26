# <ASSIGNMENT: Generate and load your data sets. Motivate your choices in the docstrings and comments. This file
# contains a suggested structure; you are free to define your own structure, adjust function arguments etc. Don't forget
# to write appropriate tests for your functionality.>

import numpy as np
import os
import numpy as np
import random
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings("ignore")


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Current file marks the root directory
TRAINING_IMAGE_DIR = os.path.join(ROOT_DIR, "data_sets", "training_images")  # Directory for storing training images
TEST_IMAGE_DIR = os.path.join(ROOT_DIR, "data_sets", "test_images")  # Directory for storing test images
LABELS = ['J', 'Q', 'K']  # Possible card labels
IMAGE_SIZE = 32 
ROTATE_MAX_ANGLE = 15
NOISE = np.arange(0,1,0.1)   # Different noise level for data set

# Mark the card type with the serial number('J': 0, 'Q': 1, 'K': 2)
LABELS_CLASS = dict((name, index) for index, name in enumerate(LABELS))

FONTS = [
    font_manager.findfont(font_manager.FontProperties(family = 'sans-serif', style = 'normal', weight = 'normal')),
    font_manager.findfont(font_manager.FontProperties(family = 'sans-serif', style = 'italic', weight = 'normal')),
    font_manager.findfont(font_manager.FontProperties(family = 'sans-serif', style = 'normal', weight = 'medium')),
    font_manager.findfont(font_manager.FontProperties(family = 'serif', style = 'normal', weight = 'normal')),
    font_manager.findfont(font_manager.FontProperties(family = 'serif', style = 'italic', weight = 'normal')),
    font_manager.findfont(font_manager.FontProperties(family = 'serif', style = 'normal', weight = 'medium')),
]  # True type system fonts


def normalize_image(raw_image: Image):
    """
    Normalize a raw image to serve as input to the image classifier.

    Arguments
    ---------
    raw_image : Image
        Raw image to normalize.

    Returns
    -------
    image : list/matrix/structure of int, int between zero and one
        Normalized image that can be used in the image classifier.
    """
    # <ASSIGNMENT: Implement your normalizer by converting pixel intensities to integers between zero and one.>
    
    # Normalize the image
    image = []
    image = np.array(raw_image) / 255.0   # Convert image data into array and normlize it
    return image


def load_data_set(data_dir, n_validation = 0):
    """
    Normalize the images in data_dir and divide in a training and validation set.

    Parameters
    ----------
    data_dir : str
        Directory of images to load
    n_validation : int
        Number of images that are assigned to the validation set
    """

    # Extract png files
    files = os.listdir(data_dir)
    png_files = []
    for file in files:
        if file.split('.')[-1] == "png":
            png_files.append(file)

    random.shuffle(png_files)  # Shuffled list of the png-file names that are stored in data_dir

    # <ASSIGNMENT: Load the training and validation set and prepare the images and labels. Use normalize_image()
    # to normalize raw images (you can load an image with Image.open()) to be processed by your
    # image classifier. You can extract the original label from the image filename.>
    training_images = []
    training_labels = []
    validation_images = []
    validation_labels = []
    # Traverse the dataset and split training and validation sets
    for i,png_file in enumerate(png_files):
        image = Image.open(f"{data_dir}/{png_file}") 
        
        # Normalize the image
        normalized_image = normalize_image(image)
        
        if i < n_validation :
            validation_images.append(normalized_image)
            validation_labels.append(LABELS_CLASS[png_file.split('_')[0]])    # Encode the labels
        else:
            training_images.append(normalized_image)
            training_labels.append(LABELS_CLASS[png_file.split('_')[0]]) 

    validation_images = np.array(validation_images)
    validation_labels = np.array(validation_labels)
    training_images = np.array(training_images)
    training_labels = np.array(training_labels)

    return training_images, training_labels, validation_images, validation_labels


def generate_data_set(n_samples, data_dir):
    """
    Generate n_samples noisy images by using generate_noisy_image(), and store them in data_dir.

    Arguments
    ---------
    n_samples : int
        Number of train/test examples to generate
    data_dir : str in [TRAINING_IMAGE_DIR, TEST_IMAGE_DIR]
        Directory for storing images
    """

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)  # Generate a directory for data set storage, if not already present

    for i in range(n_samples):
        # <ASSIGNMENT: Replace with your implementation. Pick a random rank and convert it to a noisy image through
        # the generate_noisy_image() function below.>
        
        # Pick a random rank
        rank = random.choice(LABELS)
        # Convert it to a noisy image
        noise_level = random.choice(NOISE)
        img =generate_noisy_image(rank,noise_level) 
        # img.save(f"./{data_dir}/{rank}_{i}.png")  # The filename encodes the original label for training/testing
        img.save(f"{data_dir}/{rank}_{i}.png")


def generate_noisy_image(rank, noise_level):
    """
    Generate a noisy image with a given noise corruption. This implementation mirrors how the server generates the
    raw images. However the exact server settings for noise_level and ROTATE_MAX_ANGLE are unknown.
    For the PokerBot assignment you won't need to update this function, but remember to test it.

    Arguments
    ---------
    rank : str in ['J', 'Q', 'K']
        Original card rank.
    noise_level : int between zero and one
        Probability with which a given pixel is randomized.

    Returns
    -------
    noisy_img : Image
        A noisy image representation of the card rank.
    """

    if not 0 <= noise_level <= 1:
        raise ValueError(f"Invalid noise level: {noise_level}, value must be between zero and one")
    if rank not in LABELS:
        raise ValueError(f"Invalid card rank: {rank}")

    # Create rank image from text
    font = ImageFont.truetype(random.choice(FONTS), size = IMAGE_SIZE - 6)  # Pick a random font
    img = Image.new('L', (IMAGE_SIZE, IMAGE_SIZE), color = 255)
    draw = ImageDraw.Draw(img)
    (text_width, text_height) = draw.textsize(rank, font = font)  # Extract text size
    draw.text(((IMAGE_SIZE - text_width) / 2, (IMAGE_SIZE - text_height) / 2 - 4), rank, fill = 0, font = font)

    # Random rotate transformation
    img = img.rotate(random.uniform(-ROTATE_MAX_ANGLE, ROTATE_MAX_ANGLE), expand = False, fillcolor = '#FFFFFF')
    pixels = list(img.getdata())  # Extract image pixels

    # Introduce random noise
    for (i, _) in enumerate(pixels):
        if random.random() <= noise_level:
            pixels[i] = random.randint(0, 255)  # Replace a chosen pixel with a random intensity

    # Save noisy image
    noisy_img = Image.new('L', img.size)
    noisy_img.putdata(pixels)

    return noisy_img


if __name__ == '__main__':
    generate_data_set(10000,TRAINING_IMAGE_DIR)
    generate_data_set(2000,TEST_IMAGE_DIR)
    training_images, training_labels, validation_images, validation_labels = load_data_set(TRAINING_IMAGE_DIR,2000)
    test_images, test_labels, _, _ = load_data_set(TEST_IMAGE_DIR)




