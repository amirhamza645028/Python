import datetime
DatreTime = datetime.datetime.now()
print(DatreTime.strftime("%A"))

# Time Sleping
import time
print("start")
time.sleep(2)
print("End the programe")

#  what was the fast day in this year?
today = datetime.date.today()
this_YeraFastDay = datetime.time(today.year,1,1)
print(this_YeraFastDay)
this_YeralastDay = datetime.time(today.year,12,31)
print(this_YeralastDay)

# print((datetime.datetime.now()).timestamp())
# print(datetime.datetime.now().strftime("%d/%y/%m"))
# print(datetime.datetime.today())
# print(datetime.date.today())

from datetime import datetime, timezone,timedelta
utc_time=  datetime.now(timezone.utc)+ timedelta(hours=6)
print(utc_time)

d = datetime.fromtimestamp(1760802445)

# print(d)
# print("*********************************")
# format = " %d %B,%Y"
# datetime_string = "25 December, 2022"


# d = datetime.strptime(datetime_string, format)
# print(d)

# TIME CREATE
# *******************************************
# my_date = datetime.date(2025,12,25)
# print(my_date)
# my_Time = datetime.time(10,30,45)
# print(my_Time)

# my_dateTime = datetime.datetime(2025,12,25,10,30,45)
# print(my_dateTime)

# DateTime add and minase 
# ************************************
# userdays = int(input("Enter your Add days :-"))
# Today = datetime.date.today()
# After7days = Today+ datetime.timedelta(userdays)
# print(After7days)

