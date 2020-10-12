#writing and appending to files

#appends string to the "employees.txt"
#employee_file = open("employees.txt", "a")

#adds "Toby - Human Resources" to the end of the file on the same line as the fifth employee.
#employee_file = open("employees.txt", "a")
#employee_file.write("Tody - Human Resources")
#employee_file.close()

#adds "Kelly - Customer Service" to the end of the file on a new line. 
#employee_file = open("employees.txt", "a")
#employee_file.write("\nKelly - Customer Service")
#employee_file.close()

#overwrites "employees" file with "Kelly - Customer Service"
#employee_file = open("employees.txt", "w")
#employee_file.write("Kelly - Customer Service")
#employee_file.close()

#creates a new file 
#employee_file = open("employees1.txt", "w")
#employee_file.write("\nKelly - Customer Service")
#employee_file.close()

#creates new file with different file extension
employee_file = open("index.html", "w")
employee_file.write("<p>Example that HTML can be written programatically in python</p>")
employee_file.close()