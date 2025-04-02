#list=arrays in python
numbers=[1,2,3,4,5]
"""print(numbers[0])#first
print(numbers[-1])#last
"""
#list methods
numbers.append(6)#adds 6 to the list
print(numbers)
numbers.remove(5)#removes 5 from the list
print(numbers)
print(f"length of numbers is: {len(numbers)}")
#looping through a list
for num in numbers:
    print(num)