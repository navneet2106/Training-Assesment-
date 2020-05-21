import datetime

alarmHour = int(input("Enter Hour: "))
alarmMinute = int(input("Enter Minute: "))
amPm = input("Am or Pm: ")

if amPm == "pm":
    alarmHour = alarmHour + 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
        print("WakeUP Class time")
        break


