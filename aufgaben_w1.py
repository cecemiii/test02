# Import data from the CSV file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset from downloaded csv link
url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv"
df = pd.read_csv(url, sep=",")
# Display the first few rows of the dataframe
print(df.head())

# Get the month from the date
df["Monat"] = pd.to_datetime(df["Datum"]).dt.month

# Calculate the overall average temperature
avg_temp = df["Temperatur"].mean()

# Calculate the average temperature for the month of July and May
avg_temp_july = df[df["Monat"] == 7]["Temperatur"].mean()
avg_temp_may = df[df["Monat"] == 5]["Temperatur"].mean()

print(f"The overall average temperature: {avg_temp}")
print(f"The average temperature for the month of July: {avg_temp_july}")
print(f"The average temperature for the month of May: {avg_temp_may}")
print(f"The difference in the average temperature between the months of July and May: {avg_temp_july - avg_temp_may}")