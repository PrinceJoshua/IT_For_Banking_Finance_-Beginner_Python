import csv
import numpy as np
import matplotlib.pyplot as plt
csv_file = open('MaxwellGroup-Additional-Data.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter=',')
year =[]

next(csv_file)
for row in csv_reader:
 year.append(float(row[0]))
 new_year = np.average(year)

 plot_Year = float(row[0])
 plot_AnnSalary = float(row[1])

 plt.xlabel(("Number of years"))
 plt.ylabel("Annual Salary")
 plt.scatter(plot_Year,plot_AnnSalary)
 plt.title('Salary vs. Years')


print "The Average Year of service is ", new_year
print "\nMy Comment on the data:\nThe data on this graph shows there could be a limit to the amount of money made when reaching the $60,000,\neven though the years of service was longer." \
      "Fifty Eight percent(58%) of the workers fit in this category which leads me to the\n" \
      "assumption that only having work experience may not be the major factor of getting a pay increase over the avarage pay."
plt.show()

csv_file.close()