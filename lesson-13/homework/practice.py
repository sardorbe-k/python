# 1 Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import date

birth_year = int(input("Yilingizni kiriting (masalan, 2004): "))
birth_month = int(input("Oyingizni kiriting (1-12 orasida): "))
birth_day = int(input("Kuningizni kiriting (1-31 orasida): "))

today = date.today()
birth_date = date(birth_year, birth_month, birth_day)

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    from calendar import monthrange
    prev_month_days = monthrange(today.year, today.month - 1)[1]
    days += prev_month_days

if months < 0:
    years -= 1
    months += 12

print(f"Sizning yoshingiz: {years} yil, {months} oy, {days} kun.")



# 2 Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import date, datetime

birth_year = int(input("Tug‘ilgan yilingizni kiriting (masalan, 2004): "))
birth_month = int(input("Tug‘ilgan oyingizni kiriting (1-12): "))
birth_day = int(input("Tug‘ilgan kuningizni kiriting (1-31): "))

today = date.today()

current_year_birthday = date(today.year, birth_month, birth_day)

if current_year_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)
else:
    next_birthday = current_year_birthday

days_until_birthday = (next_birthday - today).days

print(f"Sizning keyingi tug‘ilgan kuningizgacha {days_until_birthday} kun qoldi")

# 3 Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

current_date_str = input("Joriy sana va vaqtni kiriting (masalan, 2025-10-16 14:30): ")

current_datetime = datetime.strptime(current_date_str, "%Y-%m-%d %H:%M")

hours = int(input("Uchrashuv davomiyligi (soatlarda): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqalarda): "))

meeting_duration = timedelta(hours=hours, minutes=minutes)
end_time = current_datetime + meeting_duration

print(f"Uchrashuv tugaydigan sana va vaqt: {end_time.strftime('%Y-%m-%d %H:%M')}")


# 4 Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
from zoneinfo import ZoneInfo

date_str = input("Sana va vaqtni kiriting (masalan, 2025-10-16 14:30): ")
from_tz_str = input("Joriy timezone nomini kiriting (masalan, Asia/Tashkent): ")
to_tz_str = input("O‘zgartirmoqchi bo‘lgan timezone nomini kiriting (masalan, Europe/London): ")

naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

from_datetime = naive_datetime.replace(tzinfo=ZoneInfo(from_tz_str))

to_datetime = from_datetime.astimezone(ZoneInfo(to_tz_str))

print(f"\n{from_tz_str} vaqti: {from_datetime.strftime('%Y-%m-%d %H:%M')}")
print(f"{to_tz_str} vaqti: {to_datetime.strftime('%Y-%m-%d %H:%M')}")

# 5 Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

future_str = input("Kelajakdagi sana va vaqtni kiriting (masalan, 2025-12-31 23:59:59): ")

future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

print("\nHisoblash boshlandi...")

while True:
    now = datetime.now()
    remaining = future_time - now

    if remaining.total_seconds() <= 0:
        print("\n⏰ Vaqt tugadi!")
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Qolgan vaqt: {days} kun, {hours:02}:{minutes:02}:{seconds:02}", end="\r")

    time.sleep(1)

# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

email = input("Email manzilingizni kiriting: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print(" Email manzil to‘g‘ri formatda!")
else:
    print(" Email manzil noto‘g‘ri formatda!")


# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
phone = input("Telefon raqamingizni kiriting (faqat raqamlar, masalan: 1234567890): ")

digits = ''.join(filter(str.isdigit, phone))

if len(digits) == 9:
    formatted = f"({digits[:2]}) {digits[2:5]}-{digits[5:]}"
    print("Formatlangan raqam:", formatted)
else:
    print(" Noto‘g‘ri raqam uzunligi! 10 xonali raqam kiriting.")

# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

password = input("Parolingizni kiriting: ")

length = len(password) >= 8
upper = re.search(r"[A-Z]", password)
lower = re.search(r"[a-z]", password)
digit = re.search(r"\d", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

if length and upper and lower and digit and special:
    print(" Kuchli parol! (Strong password)")
elif length and (upper or lower) and digit:
    print(" O‘rtacha parol. Maxsus belgilar qo‘shing.")
else:
    print(" Zaif parol. Katta/kichik harf, raqam va maxsus belgi ishlating.")

# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

text = input("Matn kiriting:\n")
word = input("Qidirilayotgan so‘zni kiriting: ")

matches = list(re.finditer(rf"\b{re.escape(word)}\b", text, re.IGNORECASE))

if matches:
    print(f"\n'{word}' so‘zi {len(matches)} marta topildi.")
    print("Joylashuvlari (boshlanish indekslari):")
    for match in matches:
        print(f"- {match.start()} indeksda")
else:
    print(f"\n'{word}' so‘zi topilmadi.")

# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

text = input("Matn kiriting:\n")

date_pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'

dates = re.findall(date_pattern, text)

if dates:
    print("\nTopilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("\nMatnda sana topilmadi.")


