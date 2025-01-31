#Variable Declartion
name = "anash"  #String
age = 18 #Int
price = 1400.00 #Float
answer = True #Boolean
a = None #None

#Type
print(type(name))
print(type(age))
print(type(price))
print(type(answer))
print(type(a))

#Operators
"""Arithmetic Operator"""
a = 5
b = 3.40
print("Answer of Addition :",a + b)

a = 100
b = 13.40
print("Answer of Subtraction :",a - b)

a = 10
b = 3
print("Answer of Multiplication :",a * b)

a = 100
b = 4
print("Answer of Divison :",a / b)

a = 10
b = 3
print("Answer of Modulus :",a %  b)

a = 10
b = 3
print("Answer of Power :",a ** b)

"""Relational Operator"""
a = 10
b = 20
print(a == b)

a = 10
b = 20
print(a >= b)

a = 10
b = 20
print(a <= b)

a = 10
b = 20
print(a != b)

"""Assignment Operator"""
a = 1
print(a)

a += 10
print(a)

a /= 10
print(a)

a *= 2
print(a)

a %= 20
print(a)

a **= 2
print(a)

#Logical Operator
a = 10
b = 20
print((a <= b) and (a < b))

a = 10
b = 20
print((a == b) or (a <= b))

a = True
print(not a)

b = False
print(not b)

#Type Casting
a = float("2")
print(type(a))

#Type Converstion
"""Python Automatically Type Converse the datatype we don't have to do it manually"""
a = float(input("enter number :"))
b = float(input("enter number :"))
print(a + b)

