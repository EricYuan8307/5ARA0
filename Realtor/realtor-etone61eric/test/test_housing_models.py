from sklearn import base
from housing_models import *


class TestHousingModels:
    def test_train_linear_regression_model(self, clean_data_set):
        X, y = clean_data_set  # Unpack
        model, rmse_train, rmse_cv = train_linear_regression_model(X, y)
        assert issubclass(model.__class__, base.BaseEstimator)

    def test_train_decision_tree_model(self, clean_data_set):
        X, y = clean_data_set  # Unpack
        model, rmse_train, rmse_cv = train_decision_tree_model(X, y)
        assert issubclass(model.__class__, base.BaseEstimator)

    def test_train_best_model(self, clean_data_set):
        X, y = clean_data_set  # Unpack
        model = train_best_model(X, y, write_to_file=False, fit_model=False)  # Fitting takes too much time
        assert issubclass(model.__class__, base.BaseEstimator)