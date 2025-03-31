import polars as pl

def trim_rows(df: pl.DataFrame, lower_percent: float, upper_percent: float) -> pl.DataFrame:
    """
    Schneidet die ersten `lower_percent`% und die letzten `upper_percent`% der Zeilen ab.
    
    Parameter:
    - df: Das Polars DataFrame mit den Daten.
    - lower_percent: Prozentanteil der Zeilen, die von oben (Anfang) entfernt werden sollen.
    - upper_percent: Prozentanteil der Zeilen, die von unten (Ende) entfernt werden sollen.
    
    Rückgabe:
    - Ein neues DataFrame, das die verbleibenden Zeilen enthält.
    """
    total_rows = df.height
    lower_cut = int(total_rows * (lower_percent / 100.0))
    upper_cut = int(total_rows * (upper_percent / 100.0))
    
    new_length = total_rows - lower_cut - upper_cut
    if new_length <= 0:
        raise ValueError("Zu viele Zeilen werden abgeschnitten, es bleiben keine Daten übrig.")
    
    return df.slice(lower_cut, new_length)

def median_and_mean(df: pl.DataFrame, col: str) -> tuple:
    """
    Berechnet den Median und den Mittelwert (Mean) der Spalte `col` im DataFrame.
    
    Parameter:
    - df: Das Polars DataFrame mit den Daten.
    - col: Der Name der Spalte, für die der Median und der Mittelwert berechnet werden sollen.
    
    Rückgabe:
    - Ein Tuple (median, mean), das den Median und den Mittelwert der Spalte enthält.
    """
    median_value = df.select(pl.col(col).median()).item()
    mean_value = df.select(pl.col(col).mean()).item()
    return median_value, mean_value