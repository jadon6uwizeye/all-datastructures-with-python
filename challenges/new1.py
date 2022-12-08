def EmployeeNamesAndSalaries():
    employeeNames = []
    employeeSalaries = []
    employeeName = ""
    employeeSalary = 0
    sentinelValue = "done"
    averageSalary = 0
    sumOfSalaries = 0
    numberOfEmployees = 0
    difference = 0

    # prompt user for employee name
    employeeName = input("Enter employee name or done to quit: ")
    
    while( employeeName != sentinelValue):
        # prompt user for employee salary
        employeeSalary = float(input("Enter employee salary  in even hundreds. For example, a salary of 36,510 should be input as 36.5 and a salary of 69,030 should be entered as 69.0.: "))

        # store employee name and salary in parallel arrays
        employeeNames.append(employeeName)
        employeeSalaries.append(employeeSalary)

        # prompt user for employee name
        employeeName = input("Enter employee name or done to quit: ")
    

    # calculate average salary
    for i in range(len(employeeSalaries)):
        sumOfSalaries += employeeSalaries[i]

    numberOfEmployees = len(employeeSalaries)
    averageSalary = sumOfSalaries / numberOfEmployees

    # display average salary
    print("Average salary: ", averageSalary)

    # find the names and salaries of employees who's salary is within 5 of the average
    for i in range(len(employeeSalaries)):
        difference = abs(employeeSalaries[i] - averageSalary)
        if (difference <= 5):
            print("Employee name: ", employeeNames[i], " Employee salary: ", employeeSalaries[i])


EmployeeNamesAndSalaries()
