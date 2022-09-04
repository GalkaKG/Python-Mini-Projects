import datetime
from datetime import date

'''
   Here we add 7 weeks from today date to find which day gonna be.
   The weeks can change in days or hours also.
'''

today = date.today()
time_add = datetime.timedelta(weeks=7)
the_future_day = today + time_add
print(the_future_day)
