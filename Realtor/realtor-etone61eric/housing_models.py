import os

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from housing_data_loader import ROOT_DIR

MODEL_PATH = os.path.join(ROOT_DIR, "models")


# <ASSIGNMENT 3.5: Train and evaluate a linear regression model>
def train_linear_regression_model(X, y):
    """
    Train a linear regression model and report the training and cross-validation errors.

    :param X: pre-processed training features (numpy array)
    :param y: pre-processed target values for training (numpy array)
    :return: fitted model with training and cross-validation errors
    """

    # Extract a cross-validation set from the training set
    X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define a linear regression model
    linear_model = LinearRegression()

    # <FIT THE MODEL>
    linear_model.fit(X_train, y_train)
    # Predict labels for the training and cv sets
    y_train_predicted = linear_model.predict(X_train)  # <PREDICT THE TRAINING LABELS>
    y_cv_predicted = linear_model.predict(X_cv)  # <PREDICT THE CV LABELS>

    # Evaluate performance on the training and cv sets
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_predicted))
    rmse_cv = np.sqrt(mean_squared_error(y_cv, y_cv_predicted))

    return linear_model, rmse_train, rmse_cv
# </ASSIGNMENT 3.5>


# <ASSIGNMENT 3.6: Train and evaluate a decision tree model>
def train_decision_tree_model(X, y):
    """
    Train a decision tree model and report the training and cross-validation errors.

    :param X: pre-processed training features (numpy array)
    :param y: pre-processed target values for training (numpy array)
    :return: fitted model with training and cross-validation errors
    """

    # Extract a cross-validation set from the training set
    X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define a decision tree model
    tree_model = DecisionTreeRegressor()
    


    # <YOUR CODE HERE>
    tree_model.fit(X_train, y_train)

    y_train_predicted = tree_model.predict(X_train)  # <PREDICT THE TRAINING LABELS>
    y_cv_predicted = tree_model.predict(X_cv)  # <PREDICT THE CV LABELS>


    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_predicted))
    rmse_cv = np.sqrt(mean_squared_error(y_cv, y_cv_predicted))

    return tree_model, rmse_train, rmse_cv

# <QUESTION: What do you notice when comparing the training and cross-validation errors, and what does this imply?>
# The training error and cross-validation error are 0.0 and 68035.0.
# It means that the model is over-fitted. Because there is no error in training part,
# which means that the model fit all the problems in training model.
# But there is a big difference between the error and cross-validation.
# it tells us that it cannot fit the validation dataset. There is a big gap for the model
# in validation dataset

# </ASSIGNMENT 3.6>


# <ASSIGNMENT 3.7: Define and train your best model>
def train_best_model(X_train, y_train, write_to_file=True, fit_model=True):
    """
    Train your best model on the full training set.

    :param X_train: pre-processed training features (numpy array)
    :param y_train: pre-processed target values for training (numpy array)
    :param write_to_file: write model to file (Bool)
    :return: fitted model
    """

    # Define and train your best model
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(max_depth=50, max_features=8, n_estimators=200)  # <DEFINE YOUR BEST MODEL HERE>
    if fit_model:
        model.fit(X_train, y_train)

    # Store model to file (note, model is not committed to git)
    if write_to_file:
        os.makedirs(MODEL_PATH, exist_ok=True)
        model_file = os.path.join(MODEL_PATH, "model.pkl")
        joblib.dump(model, model_file)

    return model  # Return the fitted model

# <QUESTION: Report the test RMSE and motivate your model choice>
# RandomForestRegressor:
# from sklearn.ensemble import RandomForestRegressor
# Test error (RMSE): 49927.0
# Cross-validation error (RMSE): 452276.0

# DecisionTreeClassifier:
# from sklearn.tree import DecisionTreeClassifier
# Test error (RMSE): 84461.0
#Training error (RMSE): 83310.0

# MLPRegressor
# from sklearn.neural_network import MLPRegressor
# Test error (RMSE): 180450.0
# Cross-validation error (RMSE): 167866.0

# LinearRegression
# from sklearn.linear_model import LinearRegression
# Test error (RMSE): 71331.0
# # Cross-validation error (RMSE): 67820.0
#
# We should choose model that the test error and cross-validation are both small
# and close to each other. It means the model fit best.
# </ASSIGNMENT 3.7>