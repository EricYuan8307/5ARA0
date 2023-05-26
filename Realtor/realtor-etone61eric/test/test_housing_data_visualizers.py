from housing_data_visualizers import *


class TestHousingDataVisualizers:
    def test_plot_housing_data_set(self, raw_data_set):
        plot_housing_data_set(raw_data_set)
        fig = plt.gcf()
        plot_ax = fig.axes[0]
        assert plot_ax.get_xlabel().lower() == "longitude"
        assert plot_ax.get_ylabel().lower() == "latitude"
        colorbar_ax = fig.axes[1]
        assert colorbar_ax.get_label().lower() == "<colorbar>"
