# List Functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# Prints out all the elements in both lists; Adds to lists together. 
friends.extend(lucky_numbers)

# Adds item to the end of the list. 
friends.append("Creed")

# Adds item at index position 1.
friends.insert(1, "Kelly")

# Remove item from list.
friends.remove("Jim")

# Remove the entire list.
friends.clear()

# Removes last element in the list.
friends.pop()

# Prints index of the element in the list.
print(friends.index("Jim"))

# Prints how many times element appears in list.
print(friends.count("Jim"))

# Sorts list in ascending order.
friends.sort()

# Sorts a list in decending order.
friends.reverse()

# Create a copy of a list
friends2 = friends.copy()

print(friends)
