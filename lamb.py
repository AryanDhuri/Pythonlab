square=lambda x:x**2
print(square(5))
add=lambda a,b:a+b
print(add(5,3))
#lambda with map()
nums=[1,2,3,4]
squared_nums=list(map(lambda x:x**2,nums))
print(squared_nums)
#lambda with filter()
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

