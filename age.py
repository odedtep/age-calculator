from datetime import datetime

now = datetime.now()
current_date = now.strftime("%d/%m/%Y")
hour = now.strftime("%c")
hour = hour.split(" ")
hour = hour[-2]
hour = hour.split(":")
hour_now = int(hour[0])
min_now = int(hour[1])
sec_now = int(hour[2])

try:
    DOB = input("please enter your date of birth : Day / Month /Year :")
    burn_time = input('what time have your burn in the day : hour (00-24) / minute(00-60) / sec ')

    burn_time = burn_time.split("/")
    today = current_date.split("/")
    birth_hour = int(burn_time[0])
    birth_min = int(burn_time[1])
    birth_sec = int(burn_time[2])
    today_day = int(today[0])
    today_month = int(today[1])
    today_year = int(today[2])
    dob = DOB.split("/")
    birth_day = int(dob[0])
    birth_month = int(dob[1])
    birth_year = int(dob[2])
except:
    print("invailed details")

try:
    if 0 <= birth_day > 31 or 0 <= birth_month >= 13 or birth_day == " " or birth_month == " " or birth_year == " ":
        print("you have entered wrong date of birth")
        exit()
except:
    print("something went wrong , please try again.")
    exit()
try:
    if birth_hour >= 25 or birth_min >= 60 or birth_sec < 0:
        print("you have entered wrong date of birth time")
        exit()
except:
    print("something went wrong , please try again.")
    exit()

burn_hour = 0
burn_min = 0
burn_sec = 0
year = 0
month = 0
day = 0
if hour_now >= birth_hour:
    hour = hour_now - birth_hour
else:
    hour = 24 - birth_hour + hour_now
    day -= 1
if min_now >= birth_min:
    minute = min_now - birth_min
else:
    minute = 60 - birth_min + min_now
    hour -= 1
if sec_now >= birth_sec:
    second = sec_now - birth_sec
else:
    second = 60 - birth_sec + sec_now
    hour -= 1
if today_year >= birth_year:
    year = today_year - birth_year

if today_month >= birth_month:
    month = today_month - birth_month
else:
    month = 12 - birth_month + today_month
    year -= 1
if today_day >= birth_day:
    day = today_day - birth_day  # "25/12/1995"
else:
    if today_month == 3 and ((today_year % 4 == 0 and today_year % 100 != 0) or (today_year % 400 == 0)):
        day = 29 - birth_day + today_day
    else:
        day = (30 if today_month in [4, 6, 9, 11] else 31) - birth_day + today_day
        month -= 1
try:
    if year == 0 and month == 0 and day == 0 or year < 0:
        print("you  have not burn yet")
        exit()
except:
    print("somthing went wrong , please try again.")
    exit()
if year >= 0 or month >= 0 or day > 0:
    print(f"""you are {day} days  {month} months {year} years old """)
    print(f"""you are {hour} hours  {minute} minutes {second} seconds  """)
