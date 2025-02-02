import pandas as pd
import random

series = pd.Series([random.randint(1,1000) for i in range(100)])
print("ORIGINAL SERIES")
print(series)

def filter_series(series):
    arr = []
    for value in series:
        if value <= 799:
            arr.append(value)
    return pd.Series(arr)

def replace_values(series,mean_or_median):
    for i in range(len(series)):
        if series[i] > 799:
            series[i] = mean_or_median
    return series           

filtered_series = filter_series(series)
mean = int(filtered_series.mean())
median = filtered_series.median()
print(f"\nMEAN: {mean}")
print(f"MEDIAN: {median}")

series_mean = replace_values(series.copy(),mean)
series_median = replace_values(series.copy(),median)

print("\nREPLACE WITH MEAN")
print(series_mean)

print("\nREPLACE WITH MEDIAN")
print(series_median)
