#swap with three variables
a = float(input("Enter your first number :"))
b = float(input("Enter your second number :"))
temp = a
a = b
b = temp

print("a = ",a)
print("b = ",b)

#swap with two variables
a = float(input("Enter your first number :"))
b = float(input("Enter your second number :"))

a = a + b
b = a - b
a = a - b

print("a = ",a)
print("b =",b)