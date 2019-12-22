import urllib.request
import json
import csv

url = "http://nflarrest.com/api/v1/team"
f = urllib.request.urlopen(url)
data = f.read().decode("utf-8")
readfile = json.loads(data)

with open('arrest.csv','w',newline='') as arrestdata:
    csvwriter = csv.writer(arrestdata)
    count = 0
    for result in readfile:
        if count == 0:
            header = result.keys()
            csvwriter.writerow(header)
            count+=1
        csvwriter.writerow(result.values())



