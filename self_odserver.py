import pymongo
import config


def create_profile(name,age,salary):
    print("Name: ",name)
    print("Age: ",age)
    print("Salary: ",salary)

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    col = db["customers"]
    mydict = { "name": "John", "address": "Highway 37" }
    x = col.insert_one(mydict)
    print(x.inserted_id)
    print("Hello World")