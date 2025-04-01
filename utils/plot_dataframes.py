import numpy as np
import polars as pl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_column(df: pl.DataFrame,
                datetime_col: str,
                col1: str,
                sample_size: int = 10000,
                filter_value: int = 1000) -> None:
    """
    Plots the column over a datetime index.
    
    Parameters:
    - df (pl.DataFrame): The Polars DataFrame containing the columns.
    - datetime_col (str): The column name for datetime values.
    - col1 (str): The first column name.
    - sample_size (int): Number of points to sample for plotting (default=10,000).
    - filter_value (int): Maximum value to filter out (default=1,000).
    """
    # Ensure columns exist
    for col in [datetime_col, col1]:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame")

    # Convert datetime column to proper format if needed
    if not isinstance(df[datetime_col].dtype, pl.Datetime):
        df = df.with_columns(
            pl.col(datetime_col).cast(pl.Datetime).alias(datetime_col))

    # Apply filter if present
    df = df.filter(pl.col(col1) < filter_value) \
        .filter(pl.col(col1) > -filter_value)

    # Downsampling for large data
    num_rows = df.height
    if num_rows > sample_size:
        indices = np.linspace(0, num_rows - 1, sample_size, dtype=int)
        df_sampled = df[indices]
    else:
        df_sampled = df

    # Convert datetime to Python datetime for Matplotlib compatibility
    x_values = df_sampled[datetime_col].to_numpy()
    y_values = df_sampled[col1].to_numpy()

    # Plot the difference with datetime on x-axis
    plt.figure(figsize=(12, 5))
    plt.plot(x_values, y_values, label=f"{col1}", alpha=0.7, linewidth=1)

    # Format the x-axis for datetime
    plt.xlabel("Datetime")
    plt.ylabel(col1)
    plt.legend()
    plt.grid(True)

    # Format date ticks
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)

    plt.show()

def plot_columns(df: pl.DataFrame,
                 datetime_col: str,
                 columns: list[str],
                 sample_size: int = 10000,
                 filter_value: int = 1000) -> None:
    """
    Plots multiple columns over a datetime index.
    
    Parameters:
    - df (pl.DataFrame): The Polars DataFrame containing the data.
    - datetime_col (str): The column name for datetime values.
    - columns (list[str]): A list of column names to plot.
    - sample_size (int): Number of points to sample for plotting (default=10,000).
    - filter_value (int): Maximum absolute value to filter out (default=1,000).
    """
    # Ensure all required columns exist
    for col in [datetime_col] + columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame")
    
    # Convert datetime column to proper format if necessary
    if not isinstance(df[datetime_col].dtype, pl.Datetime):
        df = df.with_columns(
            pl.col(datetime_col).cast(pl.Datetime).alias(datetime_col))
    
    # Apply filter to all specified columns
    condition = pl.lit(True)
    for col in columns:
        condition = condition & (pl.col(col) < filter_value) & (pl.col(col) > -filter_value)
    df = df.filter(condition)
    
    # Downsample the DataFrame if needed
    num_rows = df.height
    if num_rows > sample_size:
        indices = np.linspace(0, num_rows - 1, sample_size, dtype=int)
        df_sampled = df[indices]
    else:
        df_sampled = df

    # Convert datetime values to a NumPy array for Matplotlib compatibility
    x_values = df_sampled[datetime_col].to_numpy()

    # Plot each column on the same figure
    plt.figure(figsize=(12, 5))
    for col in columns:
        y_values = df_sampled[col].to_numpy()
        plt.plot(x_values, y_values, label=col, alpha=0.7, linewidth=1)
    
    plt.xlabel("Datetime")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    
    # Format date ticks on the x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)
    
    plt.show()

def plot_column_difference(df: pl.DataFrame,
                           datetime_col: str,
                           cols: list[str],
                           sample_size: int = 10000,
                           filter_value: int = 1000) -> None:
    """
    Plots the difference between two columns over a datetime index.
    
    Parameters:
    - df (pl.DataFrame): The Polars DataFrame containing the columns.
    - datetime_col (str): The column name for datetime values.
    - col1 (str): The first column name.
    - col2 (str): The second column name.
    - sample_size (int): Number of points to sample for plotting (default=10,000).
    filter_value (int): Maximum value to filter out (default=1000).
    """
    col1, col2 = cols

    # Ensure columns exist
    for col in [datetime_col, col1, col2]:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame")

    # Convert datetime column to proper format if needed
    if not isinstance(df[datetime_col].dtype, pl.Datetime):
        df = df.with_columns(
            pl.col(datetime_col).cast(pl.Datetime).alias(datetime_col))

    # Compute the difference & apply filter
    df = df.with_columns((pl.col(col1) - pl.col(col2)).alias("difference")) \
        .filter(pl.col("difference") < filter_value) \
        .filter(pl.col("difference") > -filter_value)

    # Downsampling for large data
    num_rows = df.height
    if num_rows > sample_size:
        indices = np.linspace(0, num_rows - 1, sample_size, dtype=int)
        df_sampled = df[indices]
    else:
        df_sampled = df

    # Convert datetime to Python datetime for Matplotlib compatibility
    x_values = df_sampled[datetime_col].to_numpy()
    y_values = df_sampled["difference"].to_numpy()

    # Plot the difference with datetime on x-axis
    plt.figure(figsize=(12, 5))
    plt.plot(x_values,
             y_values,
             label=f"{col1} - {col2}",
             alpha=0.7,
             linewidth=1)

    # Format the x-axis for datetime
    plt.xlabel("Datetime")
    plt.ylabel("Difference")
    plt.title(f"Difference Between {col1} and {col2} Over Time")
    plt.legend()
    plt.grid(True)

    # Format date ticks
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)

    plt.show()

