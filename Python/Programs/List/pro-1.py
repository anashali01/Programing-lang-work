#customers = ["Alice", "Bob", "Charlie", "David"]
# 1.Add a new customer named "Eve" to the list.

list = ["alice" , "bob" , "charlie" , "david"]
"""list.append("eve")"""   #it add eve at the end od list
list.insert(1 , "eve")  #it add eve at the given index
print(list)


# 2.Remove "Bob" from the list.
list.remove("bob")
print(list)

# 3.Reverse the order of the list.
list.reverse()
print(list)

# 4.Return the final modified list.
print(list)