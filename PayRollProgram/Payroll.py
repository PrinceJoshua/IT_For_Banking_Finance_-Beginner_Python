import csv
from datetime import datetime
from calendar import monthrange

csv_file = open('MaxwellGroup-Payroll.csv', 'rU')
csv_reader = csv.reader(csv_file, delimiter=',')
payslips = open('payslips.csv', 'w')

payslips.write(
    "Employee   \t\t\t" + "Employee ID   \t" + "Run Date   \t" + "Pay Period   \t" + "Gross Salary   \t" + "NIS   \t"
    + "PAYE   \t" + "Pension   \t" + "Lodgement   \t" + "Net Pay" + "\n")


def slip(firstname, lastname, ID, Gross_Salary, tax, Nis, pension, Lodgement, Netpay):
    date = datetime.now()
    day = date.strftime("%d-%b-%Y")
    month = date.month
    year = date.year

    endOfMonth = str(year) + str(month) + str(monthrange(year, month)[1])

    payslips.write(firstname + " " + lastname + " \t\t" + ID + "  \t " + day + "\t  " + str(
        endOfMonth) + "    \t" + Gross_Salary + "    \t  " + tax + "\t" + Nis + "\t\t" + pension + "\t " + Lodgement + "\t\t\t" + Netpay + "\n")


def Taxband(gross_salary):
    gross_salary = float(gross_salary)
    if gross_salary >= 2083.33 and gross_salary <= 4166.67:
        gross_salary *= 0.1275
    elif gross_salary >= 4166.68 and gross_salary <= 6250.00:
        gross_salary *= 0.3235
    elif gross_salary >= 6250.00:
        gross_salary *= 0.42

    return gross_salary


def Nis(gross):
    gross_salary = float(gross)

    if gross_salary <= 4880.0:
        gross_salary *= 0.051
    else:
        gross_salary *= 0.1110

    return gross_salary


def Pension(floatgross):
    if floatgross <= 4880.00:
        floatgross *= 0.02
        return floatgross
    else:
        gross = 4800.00 * 0.02
        floatgross = (floatgross - 4880.00) * 0.025
        total = gross + floatgross

        return total


def Netpay(floatgross, Ni, Pension, tb, Lodge):
    Netpay = floatgross - (Ni + Pension + tb + Lodge)
    return Netpay


next(csv_file)
for row in csv_reader:
    grossSalary = row[6]
    lodgement = row[7]
    if lodgement == "-":
        lodgement = 0.0
    lodge = float(lodgement)

    grossSalary = float(grossSalary)
    tax = Taxband(grossSalary)
    nis = Nis(grossSalary)
    pension = Pension(grossSalary)

    Net = Netpay(grossSalary, nis, pension, tax, lodge)

    tax = float("{:.2f}".format(tax))
    nis = float("{:.2f}".format(nis))
    pension = float("{:.2f}".format(pension))
    lodge = float("{:.2f}".format(lodge))
    Net = float("{:.2f}".format(Net))

    grossSalary = str(grossSalary)
    tax = str(tax)
    nis = str(nis)
    pension = str(pension)
    lodge = str(lodge)
    Net = str(Net)

    print "Hello"

    slip(row[1], row[3], row[0], grossSalary, tax, nis, pension, lodge, Net)



payslips.close()
csv_file.close()
