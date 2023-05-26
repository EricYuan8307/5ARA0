import numpy as np
from pytest_bdd import scenario, given, when, then
from sklearn.compose import ColumnTransformer
from housing_data_pre_processor import split_housing_train_test, pre_process_housing_data
from housing_models import train_best_model


@scenario('predict_housing_prices.feature', 'Pre-process a data set')
def test_pre_process_data_set():
    pass

@scenario('predict_housing_prices.feature', 'Obtain predictions for new data')
def test_obtain_predictions():
    pass

@given("a data set")
def load_raw_data_sets(context, raw_data_set):
    context.train_set, context.test_set = split_housing_train_test(raw_data_set)


@given("a trained model on a pre-processed training set")
def trained_model(context, clean_data_set):
    X_train, y_train = clean_data_set  # Unpack
    context.model = train_best_model(X_train, y_train, write_to_file=False)


@when("I pre-process the data set for analysis")
def pre_process_data_sets(context):
    context.pipeline, context.X_train, context.y_train, context.X_test, context.y_test = \
        pre_process_housing_data(context.train_set, context.test_set, write_to_file=False)


@when("I use the trained model for prediction on new data")
def predict(context, clean_data_set):
    X_pred, _ = clean_data_set  # Unpack
    context.y_pred = context.model.predict(X_pred)


@then("I obtain a pre-processed data set")
def obtain_pre_processed_data_sets(context):
    assert type(context.pipeline) == ColumnTransformer
    assert type(context.X_train) == np.ndarray
    assert type(context.y_train) == np.ndarray
    assert type(context.X_test) == np.ndarray
    assert type(context.y_test) == np.ndarray


@then("I obtain estimated housing prices")
def obtain_estimates(context):
    assert len(context.y_pred) == 10
