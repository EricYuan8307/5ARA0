# <ASSIGNMENT: Define and interact with your model. Motivate your choices in the docstrings and comments. This file
# contains a suggested structure; you are free to define your own structure, adjust function arguments etc. Don't forget
# to write appropriate tests for your functionality.>

from data_sets import *

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras




def build_model():
    """
    Prepare the model.

    Returns
    -------
    model : model class from any toolbox you choose to use.
        Model definition (untrained).
    """

    # Set up the layers
    # The first layer: transforms the format of the images from a two-dimensional array (of 28 by 28 pixels) to a one-dimensional array (of 28 * 28 = 784 pixels).
    # Two tf.keras.layers.Dense layers: The first Dense layer has 128 nodes (or neurons). The second (and last) layer returns a logits array with length of 3.
    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(32, 32)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3)
    ])
    
    # Compile the model
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    return model



def train_model(model, n_validation, write_to_file=False):
    """
    Fit the model on the training data set.

    Arguments
    ---------
    model : model class
        Model structure to fit, as defined by build_model().
    n_validation : int
        Number of training examples used for cross-validation.
    write_to_file : bool
        Write model to file; can later be loaded through load_model().

    Returns
    -------
    model : model class
        The trained model.
    """

    training_images, training_labels, validation_images, validation_labels = \
        load_data_set(TRAINING_IMAGE_DIR, n_validation)

    # Feed the model
    print("Fit model on training data")
    history = model.fit(
        training_images,
        training_labels,
        batch_size=64,
        epochs=50,
        # We pass some validation for
        # monitoring validation loss and metrics
        # at the end of each epoch
        validation_data=(validation_images, validation_labels),
    )

    # Plot the performance figure
    acc = history.history['accuracy']                              ### Get the figure information from the history
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1,len(acc)+1)
    plt.plot(epochs,acc,'bo',label='Trainning acc')
    plt.plot(epochs,val_acc,'b',label='Vaildation acc')
    plt.legend()

    plt.figure()
    plt.plot(epochs,loss,'bo',label='Trainning loss')
    plt.plot(epochs,val_loss,'b',label='Vaildation loss')
    plt.legend()

    plt.show()

    model.summary()
    model.save('my_model.h5')

    return model


def load_model():
    """
    Load a model from file.

    Returns
    -------
    model : model class
        Previously trained model.
    """
    model = keras.models.load_model('my_model.h5')

    return model



def evaluate_model(model):
    """
    Evaluate model on the test set.

    Arguments
    ---------
    model : model class
        Trained model.

    Returns
    -------
    score : float
        A measure of model performance.
    """

    test_images, test_labels, _, _ = load_data_set(TEST_IMAGE_DIR)

    # Evaluate the model on the test data using `evaluate`
    print("Evaluate on test data")
    _, test_acc = model.evaluate(test_images, test_labels, batch_size=128)
    print("test acc:", test_acc)
    score = test_acc*100
    return score


def identify(raw_image, model):
    """
    Use model to classify a single card image.

    Arguments
    ---------
    raw_image : Image
        Raw image to classify.
    model : model class
        Trained model.

    Returns
    -------
    rank : str in ['J', 'Q', 'K']
        Estimated card rank.
    """

    image = normalize_image(raw_image)
    # Add the image to a batch where it's the only member.
    image = (np.expand_dims(image,0))
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    # predictions_single = probability_model.predict(image)
    predictions_single = probability_model(image)
    LABELS = ['J', 'Q', 'K']
    rank = LABELS[np.argmax(predictions_single[0])]
    return rank

if __name__ == '__main__':
    model = build_model()
    model_trained = train_model(model,2000,write_to_file=False)
    score = evaluate_model(model_trained)
