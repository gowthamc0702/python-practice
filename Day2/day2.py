# ==========================
# Day 2 Practice — File Handling & JSON
# ==========================

import json
from pathlib import Path

# -----------------------------------------
# Practice 1 — Save a list to a JSON file
# -----------------------------------------
data = [
    {"name": "Food", "amount": 120},
    {"name": "Travel", "amount": 400},
    {"name": "Snacks", "amount": 50}
]

# Task:
# Write "data" into a file named "expenses.json"
# Use json.dump and indent=2

# Your code:
# ...
path = Path("expenses.json")
with path.open("w") as f:
    json.dump(data,f,indent=2)


# -----------------------------------------
# Practice 2 — Read the same file back
# -----------------------------------------
# Task:
# Read "expenses.json" and store it in a variable "loaded"
# Then print loaded

# Your code:
# ...
with path.open("r") as f:
    loaded=json.load(f)
    print(loaded)


# -----------------------------------------
# Practice 3 — Append new data to the existing JSON
# -----------------------------------------
new_entry = {"name": "Shopping", "amount": 999}

# Task:
# 1. Read the existing file
# 2. Add new_entry to the list
# 3. Write it back to "expenses.json"

# Your code:
# ...
with path.open("r") as f:
    data_list=json.load(f)

data_list.append(new_entry)

with path.open("w") as f:
    json.dump(data_list,f,indent=2)
# -----------------------------------------
# Practice 4 — Pretty-print JSON
# -----------------------------------------
# Task:
# Print the final JSON content using:
# print(json.dumps(loaded, indent=2))

# Your code:
# ...
with path.open("r") as f:
    content = json.load(f)

print(json.dumps(content,indent=2))