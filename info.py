def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York" , phone="1234567890")