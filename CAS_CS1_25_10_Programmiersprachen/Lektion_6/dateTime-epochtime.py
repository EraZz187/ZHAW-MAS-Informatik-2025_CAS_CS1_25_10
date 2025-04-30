import datetime
from dateutil.parser import parse
import pytz # this module stores a list of timezones

#birthday = input("Enter your birthday (dd.mm.yyyy): ")
birthday = "11.05.1997"
day = int(birthday[0:2])
month = int(birthday[3:5])
year = int(birthday[6:])
#create a date object
birthday_dt = datetime.date(year, month, day)
today = datetime.date.today() #another date object
days_between = (today - birthday_dt).days
print("You have survived:", days_between,"days")

#create a datetime object
dt = datetime.datetime(2021, 3, 20, 13, 13, 0) # 20.3.2021, 13:13:00
now = datetime.datetime.now()
td = now - dt #td is of type timedelta, it has .days and .total_secon
print("Hours between:", int(td.total_seconds() / 3600))

# create a datetime from the epoch number:
dt = datetime.datetime.fromtimestamp(1617092100)
print(dt) # 2021-03-30 10:15:00

#use the dateutil parser to read the string in ISO 8601

t_str = "2021-03-30T17:09:00+1100" # 5:09 PM in Sydney
time1 = parse(t_str) #time1 is of type datetime
print(time1)

# use time1 from last slide (5:09 PM in Sydney)
tz_zh = pytz.timezone('Europe/Zurich')
time1 = time1.astimezone(tz_zh) # 8:09 AM in Zurich
print(time1) # 2021-03-30 08:09:00+02:00

