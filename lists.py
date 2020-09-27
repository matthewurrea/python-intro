# Lists in Python

# Lists are structures used in python to organize data
# aka Arrays

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

# Pulls data via the index value of the list. 
print(friends[0])

# Starts at the back of the list.
print(friends[-1])

# Starts at the index of 1 and pull all data going forward.
print(friends[1:])

# Grabs a range of data,for example from index 1 to 3
print(friends[1:3])

# Modifing elements in a list.
friends[1] = "Mike"
print(friends[1:])


