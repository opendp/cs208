import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
import seaborn as sns


#TODO: implement the functions below
def release_dp_quantile(x, alpha, epsilon, b=1):
    '''implement'''
    pass

def release_dp_winsorized_mean(data, epsilon, b=1):
    '''implement'''
    pass

def release_dp_laplace_mean(data, epsilon, b=1):
    '''implement'''
    pass

def rmse(a, b):
    return np.sqrt(((a - b) ** 2).sum() / len(a))

def simulate(data, bounds: List[int], epsilon=1.0, n_sims=200):
    history = []
    for b in bounds:
        for puma, subdata in data.groupby("puma"):
            target_data = subdata['income']
            for sim in range(n_sims):
                winsorized_mean, p_lower, p_upper = release_dp_winsorized_mean(target_data, epsilon, b)
                dp_mean = release_dp_laplace_mean(target_data, epsilon, b)
                history.append({
                    "puma": puma,
                    "simulation": sim,
                    "B": b,
                    "dp_mean": dp_mean,
                    "dp_winsorized_mean": winsorized_mean,
                    "p_lower": p_lower,
                    "p_upper": p_upper
                })
    return pd.DataFrame(history)

def build_boxplot(data: pd.DataFrame, history: pd.DataFrame, algorithm_names: List[str]):
    true_means = data.groupby("puma")['income'].mean()
    order = true_means.sort_values().index.tolist()
    
    melted = history.melt(
        id_vars=["B", "simulation", "puma"],
        value_vars=algorithm_names,
        var_name="algorithm",
        value_name="mean_estimate"
    )
    
    sns.set(rc={'figure.figsize': (15, 8)})
    g = sns.catplot(
        data=melted,
        kind="box",
        x="puma",
        y="mean_estimate",
        hue="algorithm",
        col="B",
        order=order,
        height=4,
        aspect=1,
        palette="Set3"
    )
    g.set_axis_labels("PUMA District", "DP Mean Estimate")
    g.set_titles("B = {col_name}")
    g.fig.subplots_adjust(top=0.9)
    
    for ax in g.axes.flatten():
        for i, puma in enumerate(order):
            true_val = true_means[puma]
            ax.plot(i, true_val, marker="o", color="red", markersize=8, linestyle="")
    return g

data = pd.read_csv("https://raw.githubusercontent.com/opendp/cs208/refs/heads/main/spring2025/data/FultonPUMS5full.csv")

# Run simulations for each bound value
bounds = [50_000, 500_000, 5_000_000]
history = simulate(data, bounds, epsilon=1, n_sims=20)

algorithm_names = ["Laplace Mean", "Winsorized Mean"]
g = build_boxplot(data, history, algorithm_names)
plt.show()
