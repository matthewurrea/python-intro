# Using the Return Statement in Functions

# Function that cubes a number. 
def cube(num):
    return num*num*num
    # return breaks out of function 'code' will not be printed
    print("code")

result = cube(4)
print(result)

