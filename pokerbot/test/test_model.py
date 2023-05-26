import os
import os
from model import *
from PIL import Image

TEST_DIR = os.path.dirname(os.path.abspath(__file__))  # Mark the test root directory
TRAINING_IMAGE_TEST_DIR = os.path.join(TEST_DIR, "data_sets", "training_images")
TEST_IMAGE_TEST_DIR = os.path.join(TEST_DIR, "data_sets", "test_images")


class TestModel:
    # <ASSIGNMENT: Test the build_model(), load_model() and evaluate_model() functions in model.py. You can use the
    # images under the test\data_sets\ directories for unit testing. You don't need to test train_model().>
    
    def test_build_model(self):
        """ Test the build_model() function in model.py. """
        model = build_model()
        assert type(model) == tf.keras.Sequential
    
    def test_load_model(self):
        """ Test the load_model() function in model.py. """
        train_model = load_model()
        assert type(train_model) == tf.keras.Sequential

    def test_evaluate_model(self):
        """ Test the evaluate_model() function in model.py. """
        trained_model = load_model()
        score = evaluate_model(trained_model)
        assert 85.0 <= score <= 100.0
    
    def test_identify(self):
        """ Test the identify() function in model.py. """
        trained_model = load_model()
        # import test images
        test_image_J = Image.open(os.path.join(TRAINING_IMAGE_TEST_DIR, "J_451.png"))
        test_image_K = Image.open(os.path.join(TRAINING_IMAGE_TEST_DIR, "K_8182.png"))
        test_image_Q = Image.open(os.path.join(TRAINING_IMAGE_TEST_DIR, "Q_5613.png"))

        assert identify(test_image_J, trained_model) == 'J'
        assert identify(test_image_K, trained_model) == 'K'
        assert identify(test_image_Q, trained_model) == 'Q'
