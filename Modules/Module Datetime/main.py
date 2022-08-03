import datetime

classDir = dir(datetime)
print(classDir)

now = datetime.datetime.now() # or now = datetime.datetime.today()
# First "datetime" is module, second "datetime" is class and "now()" is a function of datetime class.
print(now)

print("Year")
print(now.year)

print("Month")
print(now.month)

print("Day")
print(now.day)

print("Hour")
print(now.hour)

print("Minute")
print(now.minute)

print("Second")
print(now.second)

print("Microsecond")
print(now.microsecond)

infoNow = datetime.datetime.ctime(now) # This function wants a datetime object and returns more specific information about today.
print(infoNow)

print(10*"*")

# There are 2 functions of datetime class. The one of them is .strftime(String variable, formats) and
# another of them is .strptime(datetime obj, formats). strftime makes datetime objects into the string, strptime makes
# strings into the datetime objects.

# You can access the format list from this link: https://www.w3schools.com/python/python_datetime.asp
spesificInfoNow = datetime.datetime.strftime(now, "%Y")
print(spesificInfoNow)

spesificInfoNow = datetime.datetime.strftime(now, "%X")
print(spesificInfoNow)

spesificInfoNow = datetime.datetime.strftime(now, "%d")
print(spesificInfoNow)

spesificInfoNow = datetime.datetime.strftime(now, "%A")
print(spesificInfoNow)

spesificInfoNow = datetime.datetime.strftime(now, "%B")
print(spesificInfoNow)

spesificInfoNow = datetime.datetime.strftime(now, "%Y %B %A")
print(spesificInfoNow)

print(10*"*")

date1 = "29 Mayıs 2022"
gun, ay, yil = date1.split()

print(gun)
print(ay)
print(yil)

# Or we can use .strptime() function.

date2 = "15 April 2019 hour 10:12:30"
dtObjFromString = datetime.datetime.strptime(date2, "%d %B %Y hour %H:%M:%S")
print(dtObjFromString)

print(10*"*")

# You can create a datetime object with constructor.
dtWithConstructor = datetime.datetime(2022, 5, 29, 17, 46, 26, 55)
print(dtWithConstructor)

# If you do not enter the values, constructor automatically sets these values to zero.

dtWithConstructor1 = datetime.datetime(2022, 5, 29)
print(dtWithConstructor1)

print(10*"*")

# There are 2 functions which are .timestamp(datetime obj) and .fromtimestamp(int seconds)
# timestamp takes a datetime object and returns the date value as seconds.
# fromtimestamp takes integer for seconds and returns the datetime object for taken seconds.

dtObj1 = datetime.datetime.fromtimestamp(0)
print(dtObj1)

# 1970-01-01 03:00:00 is a object for beginning of the time for machines.
# If we sue timestamp(obj), function returns ((obj.date) - (1970-01-01 03:00:00)) as seconds.

secondsFromTimeStamp = datetime.datetime.timestamp(dtWithConstructor)
print(secondsFromTimeStamp)

dtObj2 = datetime.datetime.fromtimestamp(secondsFromTimeStamp)
print(dtObj2)

print(10*"*")

dtObj3 = datetime.datetime(2001, 2, 15)
now = datetime.datetime.now()

deltaTime = now - dtObj3
print(deltaTime)
print(deltaTime.days)
print(deltaTime.seconds)
# deltaTime.days + deltaTime.seconds = deltaTime

print(10*"*")

now = datetime.datetime.now()
newDate = now + datetime.timedelta(days=10) # Adds 10 days over "now".

print("Now:", now)
print("New date:", newDate)

print(10*"*")

now = datetime.datetime.now()
newDate = now + datetime.timedelta(days=10, minutes=10) # Adds 10 days and 10 minutes over "now".

print("Now:", now)
print("New date:", newDate)

