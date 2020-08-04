import datetime
year1 = int(input('Enter a  first year'))
month1 = int(input('Enter a first month'))
day1 = int(input('Enter a first day'))
date1 = datetime.date(year1, month1, day1)

year2 = int(input('Enter a second year'))
month2 = int(input('Enter a second month'))
day2 = int(input('Enter a second day'))
date2 = datetime.date(year2, month2, day2)

while(True):
    if(year2-year1==0):
        if(month2-month1<=1):
            if(day2-day1==30):
                print(1)
                break
            else:
                print(0)
                break