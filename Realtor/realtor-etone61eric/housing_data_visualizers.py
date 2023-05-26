import matplotlib.pyplot as plt


# <ASSIGNMENT 3.2: Complete the function>
def plot_housing_data_set(data_set):
    """
    Plot housing prices against geographical location.

    :param data_set: dataset to plot (DataFrame).
    """
    fig, ax = plt.subplots()
    data_set.plot(kind="scatter",
                  x="longitude",
                  y="latitude",
                  figsize=(10, 7),
                  alpha=0.3,
                  cmap=plt.get_cmap("jet"),
                  c = "median_house_value",
                  ax=ax)  # <COMPLETE THE OPTIONS>
# </ASSIGNMENT 3.2>
