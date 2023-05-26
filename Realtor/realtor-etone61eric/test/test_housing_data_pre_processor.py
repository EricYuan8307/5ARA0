from housing_data_pre_processor import *
from sklearn.compose import ColumnTransformer


class TestHousingDataPreProcessor:
    def test_split_housing_train_test(self, raw_data_set):
        train_set, test_set = split_housing_train_test(raw_data_set)
        assert type(train_set) == pd.DapytaFrame
        assert train_set.shape == (22, 10)
        assert type(test_set) == pd.DataFrame
        assert test_set.shape == (8, 10)

    def test_pre_process_housing_data(self, raw_data_set):
        train_set, test_set = split_housing_train_test(raw_data_set)
        pipeline, X_train, y_train, X_test, y_test = pre_process_housing_data(train_set, test_set, write_to_file=False)
        assert type(pipeline) == ColumnTransformer
        num_steps = [type(step[1]) for step in pipeline.transformers[0][1].steps]
        assert num_steps == [SimpleImputer, HousingAttributesExtender, StandardScaler]
        cat_steps = [type(step[1]) for step in pipeline.transformers[1][1].steps]
        assert cat_steps == [SimpleImputer, OneHotEncoder]
        assert type(X_train) == np.ndarray
        assert X_train.shape == (22, 10)
        assert type(y_train) == np.ndarray
        assert y_train.shape == (22,)
        assert type(X_test) == np.ndarray
        assert X_test.shape == (8, 10)
        assert type(y_test) == np.ndarray
        assert y_test.shape == (8,)
