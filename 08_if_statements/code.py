from datetime import datetime
day_of_week = input("What day of the week is it today?").upper()

today = datetime.now().strftime("%A")
print(f"That is {day_of_week.upper() == str(today).upper()}")

if day_of_week == "MONDAY":
    print("Have a great start to your week!")
elif day_of_week == "SATURDAY":
    print("Have a great weekend!")
else:
    print("Have a great day!")