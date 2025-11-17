import pandas as pd

df = pd.read_json("../Day2/expenses.json")

print(f"---------Original df--------\n")
print(f"{df}\n")

print("-------sorted-------")
print(df.sort_values(by="amount",ascending=False))

# print(df.describe())

print("---Selecting only name and amount")
print(df[['name','amount']])

print(df[(df['amount']>100)&(df['name']!='Travel')])

df['discounted'] = df['amount']*0.90

print(f"----Updated DF-----\n\n{df}")

df = df.drop(columns=["discounted"])

df['category']=["Essentials", "Travel", "Food", "Misc"]

print(df)

print(df.groupby("category")["amount"].sum())

grouped =df.groupby("category",as_index=False)["amount"].sum()
print(grouped)

df.to_csv("expenses_clean.csv",index=False)
df.groupby("category",as_index=False)["amount"].sum().to_csv("expenses_by_category.csv",index=False)

print("Saved : expenses_clean.csv , expenses_by_category.csv")