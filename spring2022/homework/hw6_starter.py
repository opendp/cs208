import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from typing import List


def build_boxplot(
    data: pd.DataFrame, 
    column_name: str, 

    history: pd.DataFrame, 
    algorithm_names: List[str], 

    percentile: int = None):
    """Builds a boxplot for comparing dp mean releases on PUMS.
    The red dots are exact estimates of the mean on `column_name`.

    If `percentile` is passed, history should also contain "p_lower" and "p_upper" columns of dp percentile estimates.
    If `percentile` is passed, blue (average DP estimate) and red (exact estimate) points are shown.

    :param data: PUMS dataset, as-is.
    :param column_name: Name of the column the mean is computed on.
    :param history: pd.DataFrame consisting of a "puma" column, and `algorithm_names` columns.
    :param algorithm_names: List of algorithms to plot.
    :param percentile: Option[int]
    """
    ## MAIN BOXPLOT
    melted = history.melt(
        id_vars="puma", value_vars=algorithm_names, 
        var_name="algorithm", value_name="mean estimate")

    exact_means = data.groupby("puma")[column_name].mean()
    exact_means.name = "mean"
    order = exact_means.sort_values().index

    sns.set(rc = {'figure.figsize':(15,8)})
    sns.boxplot(data=melted, 
        x="puma", y="mean estimate", hue="algorithm", 
        order=order, ax=plt.gca())

    ## EXTRA DATA POINTS
    def plot_points(series, color):
        sns.pointplot(x=series.index, y=series.values, 
            order=order, ax=plt.gca(), kind="point", linestyles='', color=color, scale=1.5)

    # plot exact means in RED
    plot_points(exact_means, "tab:red")

    if percentile is not None:
        # plot exact percentiles in RED
        exact_p_lower = data.groupby("puma")[column_name].quantile(percentile / 100 / 2)
        exact_p_lower.name = "p_lower_exact"
        plot_points(exact_p_lower, "tab:red")
        exact_p_upper = data.groupby("puma")[column_name].quantile(1 - percentile / 100 / 2)
        exact_p_upper.name = "p_upper_exact"
        plot_points(exact_p_upper, "tab:red")

        # average estimated percentiles in BLUE
        avg_lower = history.groupby("puma")['p_lower'].mean()
        avg_lower.name = "avg_lower"
        plot_points(avg_lower, "tab:blue")
        avg_upper = history.groupby("puma")['p_upper'].mean()
        avg_upper.name = "avg_upper"
        plot_points(avg_upper, "tab:blue")