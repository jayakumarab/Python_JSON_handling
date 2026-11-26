import json

student = '{"Name" : "JayaKumar","std"  : 12 ,"Department" : "Computer Science","isStudent" :true}'

data = json.loads(student)
print(data)
print(type(data))