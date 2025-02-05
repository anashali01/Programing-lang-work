#String Function

"""String Declaration"""
str1 = "This is the string.\nthis is new line" #\n use for new line in the string
str2 = 'This is the string'
str3 = """This is the string"""

print(str1)



"""Concatenation with string"""
str1 = "John "
str2 = "Deo"

print(str1 + str2)



"""Length Function in string"""
str1 = "string"   #s = 0 , t = 1 , r = 2 , i = 3 , n = 4 , g = 5

print(len(str1))


str1 = "Hello"        #H = 0 , e = 1 , l = 2 , l = 3 , o =4   == 5
str2 = " "             # (it count space) = 0  == 1
str3 = "Coders"       #C = 0 , o = 1 , d = 2 , e = 3 , r = 4 , s = 5  == 6

print(len(str1 + str2 + str3))


"""Indexing"""
#It is use to access the characters 
#We can't change the characters by targeting the index.

str1 = "This is message"    #it access the number of index which is given by user.. if we give 2 it give "h"

print(str1[1])

# str1 = "Hello"
# str1[2] = "t"  #it is not working or this is the wrong no valid

# print(str1[2])


"""Slicing"""  #mainly use in Machine learning..
#make parts of string is called slicing ..


"""Positive Index"""
str1 = "This is message"

print(str1[0 : 4])

print(str1[8 : len(str1)]) #for giving end index we can also use len function..

print(str1[8 : ]) #if we miss the last index interpreter automatically understand last index.

print(str1[ : 5]) #same work in first index..

"""Negative Index"""
str1 = "Apple"     #A = -5 , p = -4 , p = -3 , l = -2 , e = -1

print(str1[-3 : -1]) 



"""Endswith Function"""
str1 = "This is demo"  #It check that string end with given word or not.

print(str1.endswith("emo"))



"""Capitalize Function"""
str1 = "i am demo message"

print(str1.capitalize())  #it capitalize the first word of string..
print(str1)  #it works only one time if we again print the same it doesn't capitalize the first word.

str1 = "hi i am string"
str1 = str1.capitalize() #we have to store in same variable for working twice.

print(str1)