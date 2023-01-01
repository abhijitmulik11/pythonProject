#program 1-pydate
# from datetime import date
# my_date=(2022,12,7)
# print(my_date)

#program 2-current date
# from datetime import date
# my_date=date.today()
# print(my_date.year)
# print(my_date.month)
# print(my_date.day)

#program 3-python time
# from datetime import time
# my_time=(13,20,12)
# print(my_time)

#program 4-time
# from datetime import time
# my_time=(13,20,59)
# print(my_time)
#
# my_time=time(minute=12)
# print(my_time)
#
# my_time=time()
# print(my_time)

#program 5-datetime and datetime
# from datetime import datetime
# time=datetime(2022,12,8)
# print(time)
#
# time=datetime(2022,12,8,9,38,15)
# print(time)

#program 6-
# from datetime import time
# time=time(13,59,20,561214)
# print(time.hour)
# print(time.minute)
# print(time.second)
# print(time.microsecond)

#program 7
# from datetime import datetime
# date_time=datetime.now()
# print(date_time)

#program 8
# from datetime import datetime
# date_time=datetime.now()
# print(date_time)
#
# now=datetime.now()
# dt_string=now.strftime("%m %d %y  %H %M %S")
# print(dt_string)

#program 9
# import time
# t=time.localtime()
# dt=time.strftime("%H:%M:%S",t)
# print(dt)

#program 10
import datetime
print(datetime.datetime.now())
