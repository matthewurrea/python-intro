#reading from external files in python

#reading from employees.txt 
#r = read
#w = write
#a = append
#r+ = read and write 

#store open() inside a variable

employee_file = open("employees.txt", "r" )
#checks if file can be read from 
#print(employee_file.readable())

#reads first line in the file
#print(employee_file.readline())

#reads file and prints lines in a list
#print(employee_file.readlines())

#reads file and prints line at line on the specified index
#print(employee_file.readlines()[1])

#for loop using function.read
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
