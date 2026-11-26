# Python_JSON_handling
Python Json Handling Concept

Great! Let's move to the next Python topic. 🚀

# **Python JSON Handling**

JSON is very important when working with **APIs, FastAPI and backend development**.

## **1. What is JSON?**

JSON stands for **JavaScript Object Notation**.

It is a format used to store and exchange data between applications.

தமிழில்: ஒரு application-லிருந்து இன்னொரு application-க்கு data அனுப்பவும் பெறவும் JSON பயன்படுத்துகிறோம்.

Example JSON:

```
{
    "name": "Jayakumar",
    "age": 22,
    "skill": "Python",
    "is_learning": true
}
```

This is JSON data.

## **2. Python Dictionary vs JSON**

Python dictionary:

```
student = {    "name": "Jayakumar",    "age": 22,    "skill": "Python"}
```

JSON looks similar, but there are differences:

| Python                              | JSON               |
| ----------------------------------- | ------------------ |
| `True`                              | `true`             |
| `False`                             | `false`            |
| `None`                              | `null`             |
| Single or double quotes for strings | Double quotes only |

## **3. Import JSON module**

Python has a built-in `json` module.

```
import json
```

No installation required!

## **4.&#x20;**`json.dumps()`**&#x20;– Dictionary to JSON string**

```
import jsonstudent = {    "name": "Jayakumar",    "age": 22,    "skill": "Python"}data = json.dumps(student)print(data)print(type(data))
```

Output:

```
{"name": "Jayakumar", "age": 22, "skill": "Python"}
<class 'str'>
```

**Explanation:**

- `student` is a Python dictionary.
- `json.dumps()` converts the dictionary into a JSON-formatted string.
- `type(data)` returns `str`.

தமிழில்: Python dictionary-ஐ JSON string-ஆக மாற்றுவது `dumps()`.

## **5.&#x20;**`json.loads()`**&#x20;– JSON string to Dictionary**

```
import jsondata = '{"name": "Jayakumar", "age": 22}'student = json.loads(data)print(student)print(type(student))
```

Output:

```
{'name': 'Jayakumar', 'age': 22}
<class 'dict'>
```

தமிழில்: JSON string-ஐ மீண்டும் Python dictionary-ஆக மாற்றுவது `loads()`.

## **6. Important difference**

| Method         | Purpose                  |
| -------------- | ------------------------ |
| `json.dumps()` | Dictionary → JSON string |
| `json.loads()` | JSON string → Dictionary |
| `json.dump()`  | Python data → JSON file  |
| `json.load()`  | JSON file → Python data  |

## **7. Practical: Save student data in a JSON file**

**Step 1: Create&#x20;**`student.json`

```
import jsonstudent = {    "name": "Jayakumar",    "age": 22,    "department": "ECE"}with open("student.json", "w") as file:    json.dump(student, file, indent=4)print("Student data saved successfully")
```

Output:

```
Student data saved successfully
```

Your `student.json` file will contain:

```
{
    "name": "Jayakumar",
    "age": 22,
    "department": "ECE"
}
```

**Step 2: Read the JSON file**

```
import jsonwith open("student.json", "r") as file:    student = json.load(file)print(student)print(student["name"])
```

Output:

```
{'name': 'Jayakumar', 'age': 22, 'department': 'ECE'}
Jayakumar
```

## **8. Remember these four methods**

`dumps()`

Dictionary → String

`loads()`

String → Dictionary

`dump()`

Dictionary → File

`load()`

File → Dictionary

## **9. Your practice task**

Create a file called `employee.json` and save these details:

- Name: Your name
- Role: Python Developer
- Skills: Python, FastAPI, PostgreSQL
- Experience: Fresher

Use `json.dump()` to save the data and `json.load()` to read it.

## **10. Quick quiz**

**Which method converts a Python dictionary into a JSON string?**

A. `json.loads()`

B. `json.dumps()`

C. `json.load()`

D. `json.dump()`

