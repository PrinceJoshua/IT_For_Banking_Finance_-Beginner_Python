import csv
import numpy as np

data = []
average2015 = []
average2016 = []
average2017 = []
average2018 = []
average2019 = []
average2020 = []

csv_file = open('SP_GSPC.csv', 'rU')
csv_reader = csv.reader(csv_file, delimiter=',')


next(csv_file)
for row in csv_reader:
   data.append(float(row[7]))
   average = np.average(data)
   standardDv = np.std(data)

   date = row[0]
   split = date.split("/")
   spl = split[2]
   print spl

   if spl == "2015":
       average2015.append(float(row[7]))
       avg2015 = np.average(average2015)
   elif spl == "2016":
      average2016.append(float(row[7]))
      avg2016 = np.average(average2016)
   elif spl == "2017":
      average2017.append(float(row[7]))
      avg2017 = np.average(average2017)
   elif spl == "2018":
      average2018.append(float(row[7]))
      avg2018 = np.average(average2018)
   elif spl == "2019":
      average2019.append((float(row[7])))
      avg2019 = np.average(average2019)
   elif spl == "2020":
      average2020.append(float(row[7]))
      avg2020 = np.average(average2020)


print "The average rate of return for 2015 is ",avg2015
print "The average rate of return for 2016 is ",avg2016
print "The average rate of return for 2017 is ",avg2017
print "The average rate of return for 2018 is ",avg2018
print "The average rate of return for 2019 is ",avg2019
print "The average rate of return for 2020 is ",avg2020
print "The average rate of return over the 5 year period is ", average
print "The standard deviation for the rates of return over the 5 years period is ", standardDv

csv_file.close()
