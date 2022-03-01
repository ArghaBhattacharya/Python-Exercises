from datetime import date
now = date.today()
day=now.strftime("%A")
date=now.strftime("%d")
month=now.strftime("%B")
year=now.year
print("Today's date is:",day,date,month,year)