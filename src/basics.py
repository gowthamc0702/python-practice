# print("Hello world")

# character_name = "John"
# character_age = 70
# print ("There once was a man named "+character_name+",")
# print ("He was "+str(character_age)+" years old.")
# print ("He really liked the name "+character_name+" ,")
# print ("but didn't like being "+str(character_age)+" .")
# print ("but didn't like being \"\n "+str(character_age)+" .")

def greet(name):
    print("HI "+name)
    return f"Hello , {name} ! Welcome to BSK."

print(greet(input("Enter your name :")))

name ="GG"
age =23
print(f"TOP {name}, {age*10} bro")


grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]    
]

for row in grid:
    for col in row:
        print(col)
expense =[
    {
        "name":"Food",
        "amount":250.5,
        "note":"snacks"
    },
    {
        "name":"TV",
        "amount":100.75,
        "note":"Recharge"
    }
]
total=0.0
for i,e in enumerate(expense,start=1):
    total=total+e["amount"]
    print(f"{i}. | {e['name']} | {e['amount']} | {e['note']}")

print(total)