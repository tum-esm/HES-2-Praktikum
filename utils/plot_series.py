import altair as alt
import pandas as pd
import numpy as np
import polars as pl
from typing import Union

def plot_histogram_with_stats(data: Union[pl.Series, np.ndarray],
                               bin_size: float = 1.0,
                               title: str = "Histogram") -> alt.Chart:
    # Convert to NumPy if needed
    if isinstance(data, pl.Series):
        values = data.to_numpy()
    elif isinstance(data, np.ndarray):
        values = data
    else:
        raise ValueError("Input must be a Polars Series or NumPy array.")
    
    # Compute stats
    std_val = np.std(values)
    var_val = np.var(values)
    mean_val = np.mean(values)

    # Build DataFrame
    df = pd.DataFrame({'value': values})

    # Histogram chart
    hist = alt.Chart(df).mark_bar().encode(
        alt.X('value', bin=alt.Bin(step=bin_size)),
        y='count()'
    )

    # Mean line
    mean_line = alt.Chart(pd.DataFrame({'mean': [mean_val]})).mark_rule(
        color='red',
        strokeDash=[5, 5],
        size=2
    ).encode(
        x='mean:Q'
    )

    # Combine and add title
    chart = (hist + mean_line).properties(
        width=600,
        height=300,
        title={
            "text": title,
            "subtitle": [
                f"Mean: {mean_val:.2f} | Std: {std_val:.2f} | Var: {var_val:.2f}"
            ]
        }
    )

    return chart