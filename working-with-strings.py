# Working with Strings 

# \n = new line
# \" = escape character 
# \ = will insert a standart back slash 
phrase = "Giraffe Academy"

#Converts string into lowercase
print(phrase.lower())

#Converts string into uppercase
print(phrase.upper())

#Functionally check a phrase
print(phrase.isupper())

#Combination of Fucntions; converts phrase into uppercase, checks if phrase is uppercase
print(phrase.upper().isupper())

#Prints length of function
print(len(phrase))

#Grab individual characters at specific index of a string
print(phrase[0])

#Index function: tells us where a specific character or string is located inside a string
print(phrase.index("G"))

#Replace function: takes one argument and replaces it with the other
print(phrase.replace("Giraffe", "Elephant"))



