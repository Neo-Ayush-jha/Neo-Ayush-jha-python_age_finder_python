from datetime import date
def age(birthday):
    today =date.today()
    # age =today-birthday
    # return age.days
    ### normaly find
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    one_or_zero=((today.month,today.day)<(birthday.month,birthday.day))
    year_diff = today.year-birthday.year
    
    age = year_diff - one_or_zero
    
    days = age*365
    if(today.month<birthday.month):
        month_diff = birthday.month-today.month
    else:
        month_diff = today.month-birthday.month
    
    months = 12-month_diff
    days +=months*30

    months_days=today.day - birthday.day
    months_days = 30-months_days

    days += months_days
    
    count =0
    month_count =1
    for m in month_list:
        if(month_count<today.month):
            count += m-30
            month_count +=1
    
    days += count
    mo=year_diff*12
    do=mo*30
    # yo = year_diff * count
    return count
print(age(date(2001,11,1)))
print(age(date(2003,7,24)))