import random 
import time

def getRandomDate(startdate, enddate):
    print("Printing random date between", startdate, "and", enddate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startdate, dateFormat))
    endTime = time.mktime(time.strptime(enddate, dateFormat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print(getRandomDate("1/1/2020", "12/31/2020"))