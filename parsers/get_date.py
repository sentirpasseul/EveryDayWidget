import datetime
import calendar
from datetime import date, time

class TodayDateTime:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.day = self.today.day
        self.year = self.today.year
        self.time = (self.today.strftime("%H:%M"))
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
        self.full_day = f'{self.day}th of {self.month}'
        #print(self.full_day)



