from datetime import datetime, time,timedelta
# today= date.today()
# print(today)
# new_date= date(1999,12,31)
# print(new_date)

# print(time(9))
# print(time(9,2))
# print(time(9,2,2))
# print(time(9,2,2,222))

# dt=datetime(2002,10,20,14,5,2)
# print(dt)

# today=datetime.now()
# print(today)
# print(today+timedelta(days=20))

from time import localtime,strftime
# now=localtime()
# print(now)

now=strftime("%Y-%m-%d %H:%M")
now=strftime("%Y년 %m월 %d일 %H시 %M분")
print(now)