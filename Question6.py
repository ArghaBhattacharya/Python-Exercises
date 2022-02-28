try:
    from datetime import datetime
    given_date = datetime(2010, 6, 12)
    print(datetime.date(given_date).strftime('%A'))
except:
    print('Oops! An error occurred.')