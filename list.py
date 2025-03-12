my_list=[]
n=int(input("enter size"))

for i in range(n):
    a=int(input("enter a number"))
    my_list.append(a)

print(f"list={my_list}")

my_list.sort()
print(f"sorted list={my_list}")

my_list.reverse()
print(f"reversed list={my_list}")

x=int(input("enter a number"))
my_list.pop(x)
print(f"list after removing {x}={my_list}")


