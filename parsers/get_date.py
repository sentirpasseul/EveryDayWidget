import datetime
import calendar
from datetime import date, time
from datetime import datetime as dt

class TodayDateTime:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.day = self.today.day
        self.year = self.today.year
        self.months = ['January', 'February', 'March', 'April',
                       'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        self.month = self.months[self.today.month-1]
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.weekday = self.weekdays[calendar.weekday(self.year, self.today.month, self.day)]
        #print(self.today)
        #print('День: ',self.day)
        #print("Месяц: ",self.month)
        #print('День недели: ', self.weekday)
        #print("Время: ",self.time)
        self.full_day = f'{self.day}{self.get_day()} of {self.month}'
        #print(self.full_day)

    def get_day(self):
        day = self.day
        if day < 2:
            return 'st'
        elif 1 < day < 3:
            return 'nd'
        elif day == 3:
            return 'rd'
        elif day > 3:
            return 'th'



