people={
    "contact":{"aryan":8080178546,
               "mom":7066566439,
               "bro":9293940843
               }
}

name=input("enter name")
for contacts,details in people.items():
    if name in details:
        print(f"{name}:{details[name]}")