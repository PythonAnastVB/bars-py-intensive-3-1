import datetime
def get_next_date(some_date):
    """Возвращает следующую дату для заданной
    Args:
        some_date: определенная исходная дата
    Returns: следующая дата
    """
    d1=datetime.datetime.strptime(some_date, '%Y-%m-%d')
    if d1.month in [1, 3, 5, 7, 8, 10, 12]:
        if d1.day!=31:
            next_day=d1.day+1
            next_date=datetime.date(d1.year, d1.month, next_day)
            print(next_date)
        elif d1.day==31 and d1.month==12:
            next_day=1
            next_month=1
            next_year=d1.year+1
            next_date=datetime.date(next_year, next_month, next_day)
            print(next_date)
        else:
            next_day=1
            next_month=d1.month+1
            next_date=datetime.date(d1.year, next_month, next_day)
            print(next_date)               
    elif d1.month in [4, 6, 9, 11]:
        if d1.day!=30:
            next_day=d1.day+1
            next_date=datetime.date(d1.year, d1.month, next_day)
            print(next_date)
        else:
            next_day=1
            next_month=d1.month+1
            next_date=datetime.date(d1.year, next_month, next_day)
            print(next_date) 
    elif d1.month == 2:
        if d1.day!=28:
            next_day=d1.day+1
            next_date=datetime.date(d1.year, d1.month, next_day)
            print(next_date)
        else:
            next_day=1
            next_month=d1.month+1
            next_date=datetime.date(d1.year, next_month, next_day)
            print(next_date)
    
    
    
    
