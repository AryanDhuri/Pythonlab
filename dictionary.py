"""student={
    "name":"Olive",
    "age":20,#no double quotes for numbers
    "grade":"A"
}
print(student["age"])
#adding and removing elements
student["city"]="new york"#adding
del student["age"]
#looping dictionaries
for key,value in student.items():#use .items()for printing values 
    print(f"{key}={value}")"""

#looping through nested dictionaries
student={
    "alice":{"age":18,"class":"1_A"},
    "bob":{"age":19,"class":"1_B"}
}
for name,details in student.items():
    print(f"Student: {name}")
    for key,value in details.items():
        print(f"{key}={value}")
