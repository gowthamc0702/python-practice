import pandas as pd

# Step 1 — Load your JSON file
df = pd.read_json("../Day2/expenses.json")

print("\n--- DataFrame Loaded ---")
print(df)

# Step 2 — Basic inspection
print("\n--- Head (first 5 rows) ---")
print(df.head())

print("\n--- Info ---")
print(df.info())

print("\n--- Describe (summary stats) ---")
print(df.describe())

# Step 3 — Select columns
print("\n--- Amount column only ---")
print(df['amount'])

# Step 4 — Filter rows
print("\n--- Expenses > 100 ---")
print(df[df['amount'] > 100])

# Step 5 — Add new column
df['taxed'] = df['amount'] * 1.05
print("\n--- Added taxed column ---")
print(df)

# Step 6 — Save new DataFrame
df.to_csv("expenses_with_tax.csv", index=False)
print("\nSaved: expenses_with_tax.csv")
