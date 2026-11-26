import json

student = {
    "Name" : "Jayakumar",
    "Std"  : 12,
    "Department" : "Computer science",
    "isStudent" : True
}

data = json.dumps(student)
print(data)
print(type(data))

