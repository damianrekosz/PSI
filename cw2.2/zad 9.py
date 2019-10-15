import random
import datetime
#tuple z poprzedniego zad
students = (random.randrange(100000,999999), random.randrange(100000,999999), random.randrange(100000,999999),
            random.randrange(100000,999999), random.randrange(100000,999999), random.randrange(100000,999999),
            "jan kowalski", "adam zakrzewski", "wiktor wiśniewski", "marta dąbrowska", "iwona kłosińska", "józef śliwowski")

studentsDict = dict()
for i in range((students.__len__()/2).__int__()):
    studentsDict[students[i+6]] = students[i]

print (studentsDict)
data = []
for i in range(6):
    birth = 20+i
    birthDate = datetime.date.fromisoformat('1997-11-' + birth.__str__())
    data.extend([birthDate, 2019 - birthDate.year, "student" + (i+22).__str__() + "@uwm.edu.pl", "ul.studencka " + i.__str__() + ", 10-032 Olsztyn"])


for i in range(6):
    for j in range(4):
        studentsDict[j + i*4] = data[j + i*4]

print (studentsDict)