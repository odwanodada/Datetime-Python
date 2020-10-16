from datetime import date
from datetime import time
from datetime import  datetime,timedelta
d = date(2020, 8, 22)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d"))#%Y is year %m is month %d is day

t = time(1, 30, 00)
print(t.hour)
print(t.minute)
print(t.second)
print(t.strftime("%H: %M: %S"))#%H is hour %M is minutes %S is seconds

dt = datetime(2020, 10, 16, 11,22,50)
############For loop
for i in range(10):
    print(dt)
    dt=dt +timedelta(days=14)

########################### while loop
mydate = datetime(2020, 12, 15, 1,30,00)
x = 0
while x < 10:
    print(mydate)
    mydate= mydate +timedelta(days=14)
    x = x + 1



