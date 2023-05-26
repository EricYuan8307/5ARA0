import copy
import numpy as np
from housing_attributes_extender import HousingAttributesExtender


class TestHousingAttributesExtender:
    def test_init_defaults(self):
        extender = HousingAttributesExtender()
        assert extender.add_bedrooms_per_room

    def test_fit(self):
        extender = HousingAttributesExtender()
        extender_copy = copy.deepcopy(extender)
        extender.fit([])
        assert extender.__dict__ == extender_copy.__dict__  # Test that attributes are unchanged

    def test_transform(self):
        extender = HousingAttributesExtender()
        X = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
        X_trans = extender.transform(X)
        assert all(X_trans[:, 6] == [5/4, 11/10])
