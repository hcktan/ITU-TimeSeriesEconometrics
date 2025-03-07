

#%%

# ECN 407E - Time Series Econometrics - CRN: 22858 
# Hcktan
# 

# Assignment 1 - Question 1 Code Block

#%%

import pandas as pd
import matplotlib.pyplot as plt
 
#%%

# File path, file name, and sheet name specified.

file_path = r"C:\Users\Hcktan\Desktop\Ders Dosyaları\Time Series Econometrics\Assignments\HW 1\Source\hw1_q1_agemp.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Date format checked and first columns displayed for control purposes.
df["date"] = pd.to_datetime(df["date"])
print(df.head())

#%% 

# Visualization using matplotlib.

plt.figure(figsize=(10, 5))  # Set figure size.
plt.plot(df["date"], df["agemp"], color="red", linewidth=2)  # Line plot details.

# Set title and labels.
plt.title("Employment in Agriculture and Related Industries\n(Seasonally Adjusted)", fontsize=20)
plt.xlabel("Months", fontsize=15)
plt.ylabel("Employment (Thousands)", fontsize=15)

# Make x-axis more readable.
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=1.0)  # Background grid.

plt.show()

#%%

# Calculate moving average to observe general trend in the data.
# 12-month moving average calculated.

df["rolling_mean"] = df["agemp"].rolling(window=12, center=True).mean()

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["agemp"], color="lightgray", linewidth=2, label="Original Data")  # Raw data
plt.plot(df["date"], df["rolling_mean"], color="red", linewidth=2, label="12-Month Moving Average")  # Trend line

# Set title and labels.
plt.title("Trend Analysis of Employment in Agriculture", fontsize=20)
plt.xlabel("Months", fontsize=15)
plt.ylabel("Employment (Thousands)", fontsize=15)
plt.legend()
plt.grid(True, linestyle="--", alpha=1.0)

plt.show()

#%%

# Focused analysis on the year 2018.

# Filter data for 2018.
df_2018 = df[(df["date"] >= "2018-01-01") & (df["date"] <= "2018-12-31")]

plt.figure(figsize=(10, 5))
plt.plot(df_2018["date"], df_2018["agemp"], marker="o", color="red", linewidth=2, label="2018 Data")

# Set title and labels.
plt.title("Employment in Agriculture - 2018", fontsize=20)
plt.xlabel("Months", fontsize=15)
plt.ylabel("Employment (Thousands)", fontsize=15)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.show()
