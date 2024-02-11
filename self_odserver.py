import config
from datatype import userProfile
from icecream import ic
from datetime import datetime
def insertExpense(col,db):
    username = input("Enter username: ")
    expenseName = input("Enter expense name: ")
    expenseAmount = float(input("Enter expense amount: "))
    expenseDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    col.find_one({"username": username})
    new_col = db["expenses"]
    new_col.insert_one({"username": username, "expenseName": expenseName, "expenseAmount": expenseAmount, "expenseDate": expenseDate})

if __name__ == "__main__":
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    salary = float(input("Enter your salary: "))
    my_profile = vars(userProfile(name, age, salary))
    db = config.mongo_client["cluster0"]
    col = db["data"]
    if col.find_one({"name": name}):
        print("Profile already exists")
        exit()
        
    x = col.insert_one(my_profile)
    
    
    print("Profile created successfully")
    ic(my_profile)
