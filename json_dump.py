import json

student = {
    "Name" : "Jayakumar",
    "Std"  : 12,
    "Department" : "Computer science",
    "isStudent" : True
}

with open("student.json","w") as file :
    json.dump(student,file,indent = 4)

print("File saved Successfully")