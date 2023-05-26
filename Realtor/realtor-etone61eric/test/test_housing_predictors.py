from housing_predictors import *

TEST_DIR = os.path.dirname(os.path.abspath(__file__))  # Mark the test root directory


class TestHousingPredictors:
    def test_predict_median_house_value(self, raw_data_set):
        y_pred = predict_median_house_value(raw_data_set, pipeline_path=TEST_DIR, model_path=TEST_DIR)
        assert len(y_pred) == 30
