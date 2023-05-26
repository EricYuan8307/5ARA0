import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class HousingAttributesExtender(BaseEstimator, TransformerMixin):
    """
    A custom step in the data pre-processing pipeline that adds interaction-features.
    """

    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # Nothing to do

    # <ASSIGNMENT 3.3: Complete the transform function>
    def transform(self, X):
        """
        Append a bedrooms per room feature to X.

        :param X: numpy array
        :return: numpy array
        """

        total_rooms = X[:, 3]
        total_bedrooms = X[:, 4]
        if self.add_bedrooms_per_room:
            X = np.hstack([X, (total_bedrooms.astype("float") / total_rooms).reshape(X.shape[0], 1)])

        return X
    # </ASSIGNMENT 3.3>
