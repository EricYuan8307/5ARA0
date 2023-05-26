import os
import pytest
import pandas as pd
import numpy as np
from housing_data_loader import load_housing_data, sanitize_data_entry

TEST_DIR = os.path.dirname(os.path.abspath(__file__))  # Mark the test root directory


class TestHousingDataLoader:
    def test_sanitize_data_entry(self):
        # Define feature names and categories for testing
        features = ["first_feature", "second_feature", "third_feature"]
        categories = {"second_feature": ["A", "B"],
                      "third_feature": ["C", "D"]}

        # <ASSIGNMENT 2.1: Complete the test>
        # Valid modes
        assert sanitize_data_entry("first_feature", "1", features, categories) == ("first_feature", 1.0)
        assert sanitize_data_entry("second_feature", "A", features, categories) == ("second_feature", "A")
        assert sanitize_data_entry("first_feature", '', features, categories) == ("first_feature", np.nan)
        # Invalid modes

        assert pytest.raises(ValueError, sanitize_data_entry, "first_feature", "1.0j", features, categories)
        assert pytest.raises(ValueError, sanitize_data_entry, "second_feature", " ", features, categories)
        assert pytest.raises(ValueError, sanitize_data_entry, "third_feature", "Yuan", features, categories)
        # </ASSIGNMENT 2.1>

    def test_load_housing_data(self):
        data = load_housing_data(data_path=TEST_DIR)
        assert type(data) == pd.DataFrame
        assert len(data) == 30  # Our data set for the test suite has only thirty entries
        assert len(data.columns) == 10
