import pandas as pd

# Create DataFrame from dictionary
data = {
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 70]
}

df = pd.DataFrame(data)

# Display DataFrame
print("===== ORIGINAL DATAFRAME =====")
print(df)

# Add new column (calculated values)
df["Percentage"] = df["Marks"] / 100 * 100   # (just example calculation)

# Display updated DataFrame
print("\n===== UPDATED DATAFRAME =====")
print(df)
