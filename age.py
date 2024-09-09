from datetime import datetime


def is_leap_year(year):
    return ((year % 4 == 0 and year % 100 != 0)
            or (year % 400 == 0))


def get_star_sign(day, month, year):
    if month == 2 and day > 29:
        return "Invalid date for February"
    if month == 2 and day == 29 and not is_leap_year(year):
        return "Invalid date: Not a leap year"

    if month == 12:
        return 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        return 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        return 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        return 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        return 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        return 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        return 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        return 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        return 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        return 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        return 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        return 'Scorpio' if (day < 22) else 'Sagittarius'
    return 'Unknown'


def get_chinese_zodiac(year):
    zodiac_animals = [
        'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat',
        'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
        'Horse', 'Goat']
    return zodiac_animals[year % 12]


now = datetime.now()

try:
    dob_str = input("Please enter your date of birth "
                    "(Day/Month/Year): ")
    birth_time_str = input("What time were you born "
                           "(Hour(00-24)/Minute(00-60)/Second): ")

    dob = datetime.strptime(dob_str, "%d/%m/%Y")
    birth_time = datetime.strptime(birth_time_str, "%H/%M/%S").time()

    birth_datetime = datetime.combine(dob.date(), birth_time)

    if birth_datetime > now:
        print("You haven't been born yet!")
        exit()

    age_years = now.year - dob.year
    age_months = now.month - dob.month
    age_days = now.day - dob.day

    if age_days < 0:
        age_months -= 1
        if now.month == 3 and is_leap_year(now.year):
            age_days += 29
        else:
            age_days += (30 if now.month in [4, 6, 9, 11] else 31)

    if age_months < 0:
        age_years -= 1
        age_months += 12

    time_diff = now - birth_datetime
    total_seconds = time_diff.total_seconds()
    hours = int(total_seconds // 3600 % 24)
    minutes = int(total_seconds // 60 % 60)
    seconds = int(total_seconds % 60)

    star_sign = get_star_sign(dob.day, dob.month, dob.year)
    chinese_zodiac = get_chinese_zodiac(dob.year)

    print(f"\nYou are {age_years} years, "
          f"{age_months} months, and {age_days} days old.")
    print(f"With exact time of: {hours} hours, "
          f"{minutes} minutes, and {seconds} seconds.")
    print(f"Your star sign is: {star_sign}")
    print(f"Your Chinese Zodiac sign is: {chinese_zodiac}")

except ValueError:
    print("Invalid date or time format! Please try again.")
