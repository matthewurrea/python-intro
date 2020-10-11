#try except block 
#catching errors in python

#number = int(input("Enter a number: "))
#print(number)

#enter something other than a number will throw an error (ie. "alsdjf")

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print(error)

#using only except is too broad; define the error

