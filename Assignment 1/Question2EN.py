# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 17:26:46 2025

@author: Haktan Ö
"""

#%%

# ECN 407E - Time Series Econometrics - CRN: 22858 
# Yusuf Haktan Öztürkçü
# 070190421

# Assignment 1 - Question 2 Code Block

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # !pip install statsmodels

#%%

# Specify the file path, file name, and sheet name to be used.

file_path = r"C:\Users\Haktan Ö\Desktop\Ders Dosyaları\Time Series Econometrics\Assignments\HW 1\Source\hw1_q2_macro.xlsx"  # Enter the file name
df = pd.read_excel(file_path, sheet_name="all")  # Sheet name

# Check date format and display the first columns for verification.

print(df.head())

#%%

# Convert GDP and TAX data into real values.

df["rgdp"] = df["gdp"] / df["cpi"]  # Define real GDP and real TAX variables.
df["rtax"] = df["tax"] / df["cpi"]

# Compute logarithms of the real values.

df["lrgdp"] = np.log(df["rgdp"])  # Apply log transformation to real GDP.
df["lrtax"] = np.log(df["rtax"])  # Apply log transformation to real TAX.

# Display the transformed values for verification.
print(df[["rgdp", "rtax", "lrgdp", "lrtax"]].head())

#%%

# Plot Time Series Graph.

plt.figure(figsize=(10,5))  # Set figure size.
plt.plot(df["date"], df["lrgdp"], label="Log(RGDP)", color="blue", linewidth=2)
plt.plot(df["date"], df["lrtax"], label="Log(RTAX)", color="red", linewidth=2)

# Set title and labels.
plt.title("Log of Real GDP and Real Tax Over Time", fontsize=20)
plt.xlabel("Year", fontsize=15)
plt.ylabel("Log Values", fontsize=15)
plt.legend()
plt.grid(True, linestyle="--", alpha=1.0)
plt.show()

#%%

# Plot XY Scatter Plot.

plt.figure(figsize=(8,6))  # Set figure size.
plt.scatter(df["lrgdp"], df["lrtax"], color="red", alpha=1.0)

# Set title and labels.
plt.title("Scatter Plot of LRTAX vs LRGDP", fontsize=20)
plt.xlabel("LRGDP", fontsize=15)
plt.ylabel("LRTAX", fontsize=15)
plt.grid(True, linestyle="--", alpha=1.0)
plt.show()

#%%

# Estimate the Regression Model.

# Check for missing values before regression.
print(df[["lrgdp", "lrtax"]].isna().sum())  # Count missing values.
print(df[["lrgdp", "lrtax"]].describe())  # Display general statistics of the data.

# Handle missing values and infinite values.
df_clean = df[["lrgdp", "lrtax"]].replace([np.inf, -np.inf], np.nan)  # Convert infinite values to NaN.
df_clean = df_clean.dropna()  # Remove rows with NaN values.

# Define independent and dependent variables.
X = sm.add_constant(df_clean["lrgdp"])  # Independent variable.
y = df_clean["lrtax"]  # Dependent variable.

# Fit the OLS regression model.
model = sm.OLS(y, X).fit()
print(model.summary())

#%%

# An error occurred due to a mismatch in the number of values on the X-axis (year) and Y-axis (residuals)/
# Data was aligned due to missing values in certain rows.
df_clean = df.dropna(subset=["lrgdp", "lrtax"])

# Plot Residuals from Regression.
plt.figure(figsize=(10,5))  # Set figure size.
plt.plot(df_clean["date"], model.resid, color="red", label="Residuals")  # Use df_clean instead of df.

# Set horizontal reference line at zero.
plt.axhline(0, linestyle="--", color="black")

# Set title and labels.
plt.title("Residuals from Regression", fontsize=20)
plt.xlabel("Year", fontsize=15)
plt.ylabel("Residuals", fontsize=15)
plt.legend()
plt.grid(True, linestyle="--", alpha=1.0)
plt.show()
