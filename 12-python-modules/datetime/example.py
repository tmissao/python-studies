import datetime

# Creates a Data representing today
today = datetime.date.today()

# Creates a Time object
datetime.time(12,0,30)

# Creates a datetime
mytime = datetime.datetime(2021,2,11,11,53,23)
print(mytime)

# Updates Date
mytime = mytime.replace(year = 2022)

# Date Math
date1 = datetime.datetime(2021,2,11,11,53,23)
date2 = datetime.datetime(2022,2,11,12,00,23)
timebetween = date2 - date1
print(timebetween.total_seconds())

date1 = datetime.date(2021,2,11)
date2 = datetime.date(2022,2,11)
timebetween = date2 - date1
print(timebetween)
