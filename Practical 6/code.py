a = int(input("Enter the first number: "))
b = int(input("Enter the second integer: "))

c = a
d = b

#the temp method
print("The Temp method: ")
print("A and B before the swapping are", a, "and", b)
temp = a
a = b
b = temp
print("A and B after the swapping are", a, "and", b)

#the a,b = b,a method
print("The a,b=b,a method: ")
print("A and B before the swapping are", c, "and", d)
c, d = d, c
print("A and B after the swapping are", c, "and", d)
