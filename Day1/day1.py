# ==========================
# Day 1 Practice — List Comprehensions, Lambda, Map, Filter, Zip, Enumerate
# ==========================


# -----------------------------------------
# Practice 1 — Filter + Map Combo
# -----------------------------------------
# Given:
nums = [5, 12, 30, 7, 50, 3]

# Task:
# 1) Keep only numbers > 10
# 2) Double them
# 3) Store final result in "result"
# Example output: [24, 60, 100]

result = list(map(lambda y:y*2,(filter(lambda x:x>10,nums))))
print("Practice 1:", result)



# -----------------------------------------
# Practice 2 — Convert Two Lists to List-of-Dicts
# -----------------------------------------
# Given:
names = ["Food", "Travel", "Snacks"]
amounts = [120, 400, 50]

# Task:
# Build this using zip + list comprehension:
# [
#   {"name":"Food", "amount":120},
#   {"name":"Travel","amount":400},
#   {"name":"Snacks","amount":50}
# ]

expenses = list({"name":a,"amount":b} for a,b in zip(names,amounts))
print("Practice 2:", expenses)



# -----------------------------------------
# Practice 3 — Enumerate to Create ID-Tagged Items
# -----------------------------------------
# Given:
categories = ["Home", "Bills", "Shopping"]

# Task:
# Create using enumerate + list comprehension:
# [
#   {"id": 0, "category": "Home"},
#   {"id": 1, "category": "Bills"},
#   {"id": 2, "category": "Shopping"}
# ]

tagged = list({"id":i,"category":l}for i,l in enumerate(categories))
print("Practice 3:", tagged)



# -----------------------------------------
# Practice 4 — Name Length Calculator
# -----------------------------------------
# Given:
items = ["Food", "Travel", "Stationery"]

# Task:
# Create this using list comprehension:
# [
#   {"item":"Food", "length":4},
#   {"item":"Travel","length":6},
#   {"item":"Stationery","length":10}
# ]

lengths = list({"item":a,"length":b} for a,b in zip(items,map(lambda x:len(x),items)))
print("Practice 4:", lengths)



# -----------------------------------------
# Practice 5 — map() with Two Lists
# -----------------------------------------
# Given:
a = [2, 4, 6]
b = [10, 20, 30]

# Task:
# Use map(lambda x, y: x * y) to produce:
# [20, 80, 180]

products = list(map(lambda x,y:x*y,a,b))
print("Practice 5:", products)
