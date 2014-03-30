from hashtable import Hashtable
from hashtable import hashFunction
import csv

cities = open("uscities.txt", "r")
datafile = open("datafile.csv", "w")
c = csv.writer (datafile, dialect = "excel")

citylist = []

for line in cities:
    line = line.split(",")
    citylist.append(line)


numbuck = 1000    
hashy = Hashtable(hashFunction, numbuck)    
for lists in citylist:
    hashy[lists[1]] = lists[4] # can be anything

count = 0
datalist = []
genobj = hashy.getBucketSizes()
for item in genobj:
    c.writerow([count, item])
    count += 1

cities.close()
datafile.close()