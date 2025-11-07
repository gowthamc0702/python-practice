from pathlib import Path
import json

expense=[]
add_new=True


def new_expense():
    expense_name=input("Enter expense name: ")
    try:
        expense_amount=float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount")
        expense_amount=float(input("Enter amount: "))
    
    expense_note=input("Enter note (optional): ")
    
    return{
        "name":expense_name,
        "amount":expense_amount,
        "note":expense_note
    }


while add_new:
    data=new_expense()
    expense.append(data)
    Isvalid_option=True
    while Isvalid_option:
        option=input("Add another? (y/n): ")
        if(option in "Yy"):
            data=new_expense()
            expense=expense.append(data)
        elif(option in "Nn"):
            Isvalid_option=False
            add_new=False
        else:
            print("Enter correct option (y/n)")

output_path= Path("expense.json")

if output_path.exists():
    with output_path.open("r",encoding="utf-8") as f:
        try:
            existing=json.load(f)
            if isinstance(existing,list):
                expense=existing+expense
            
        except json.JSONDecodeError:
            pass

        
#print(expense)
#i dont want to just print , i want in json format

with output_path.open("w",encoding="utf-8") as f:
    json.dump(expense,f,indent=2,ensure_ascii=False)

print(f"\n\n Saved {len(expense)} expense(s) to {output_path}")
all_expense=""
while True:
    view=input("Do you want to view all expenses in file? (y/n)")
    if(view.lower()=="y"):
        with output_path.open('r',encoding='utf-8') as f:
            try:
                all_expense=json.load(f)
            except :
                pass
            
            print(json.dumps(all_expense,indent=2,ensure_ascii=False))
            break
    elif(view.lower()=="n"):
        break
    else:
        print("enter right option y or n")