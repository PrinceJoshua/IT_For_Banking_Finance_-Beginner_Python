def SalaryCalc(employeeType):
    if employeeType == "1":
        employeeSalary = 1000
        print "Employee Salary is $%2.f : " % employeeSalary

    if employeeType == "2":
        employeeRate = raw_input("Please Enter employee Rate\n")
        employeeRate = float(employeeRate)
        employeeHours = raw_input("Please enter Hours Work\n")
        employeeHours = int(employeeHours)

        if employeeHours == 40:
            employeeSalary = employeeRate * 40
            print "Employee Salary is $%2.f : " % employeeSalary
        else:
            overTime = (employeeHours - 40) * 1.5
            employeeSalary = (40 * employeeRate) + overTime
            print "Employee Salary is $%2.f : " % employeeSalary

    if employeeType == "3":
        grossSalesPerWeek = raw_input("What are your Gross Sales per Week?\n")
        grossSalesPerWeek = float(grossSalesPerWeek)
        employeeSalary = 215 + (0.053 * grossSalesPerWeek)
        print "Employee Salary is $%2.f : " % employeeSalary

    if employeeType == "4":
        ratePerItem = raw_input("What the rate per Item\n")
        ratePerItem = float(ratePerItem)
        numOfItem = raw_input("What is the number of Items Prodoced\n")
        numOfItem = float(numOfItem)

        employeeSalary = ratePerItem * numOfItem
        print "Employee Salary is $%2.f : " % employeeSalary

employeeType = raw_input("Please enter employee Type : \nEnter 1 - Manager \nEnter 2 - Hourly employee \nEnter 3 - Commission worker \nEnter 4 - Task worker \n")

SalaryCalc(employeeType)