from data_sets import *
import os
import numpy as np
import pytest

TEST_DIR = os.path.dirname(os.path.abspath(__file__))  # Mark the test root directory
TRAINING_IMAGE_TEST_DIR = os.path.join(TEST_DIR, "data_sets", "training_images")
TEST_IMAGE_TEST_DIR = os.path.join(TEST_DIR, "data_sets", "test_images")


class TestDataSets:
    # <ASSIGNMENT: Test the normalize_image(), load_data_set() and generate_noisy_image() functions in
    # data_sets.py. You can use the images under the test\data_sets\ directories for unit testing.
    # You don't need to test generate_data_set().>
    def test_normalize_image(self,image):
        '''
        Test normalize_image function
        '''
        # normalize the image
        test_image = normalize_image(image)
        # check the data if it is normalized, the value should in between 0.0 and 1.0
        assert np.max(test_image) <= 1.0
        assert np.min(test_image) >= 0.0

        # check the feature shape 
        assert test_image.shape == (32,32)
        
    def test_load_data_set(self):
        '''
        Test load_data_set() function if it split traning sets and validation sets porperly
        '''

        training_images, training_labels, validation_images, validation_labels = load_data_set(TRAINING_IMAGE_TEST_DIR,1)
        # validation set should contain 1 element
        assert len(validation_images) == 1 and len(validation_labels) == 1
        # training set should contain 2 elements
        assert len(training_labels) == 2 and len(training_images) == 2
        
    
    
    def test_generate_noisy_image(self):
        '''
        Test generate_noisy_image() function if it generate image as required
        '''  
        # If noise level is out of the range, raises error
        assert pytest.raises(ValueError, generate_noisy_image, "J", 8.8)
        # If rank is out of the range, raises error
        assert pytest.raises(ValueError, generate_noisy_image, "A", 0.6)
        # Test whether the shape of the generated image meets the requirement
        generated_image_example = generate_noisy_image("K", 0.5)
        assert generated_image_example.size == (32, 32)

