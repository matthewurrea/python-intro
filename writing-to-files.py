#writing and appending to files

employee_file = open("employees.txt", "a")

#adds "Toby - Human Resources to the end of the file"
employee_file.write("Tody - Human Resources")

employee_file.close()

