import datetime
import calendar
from datetime import date, time

class TodayDateTime:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.day = self.today.day
        self.month = self.today.month
        self.year = self.today.year
        self.time = (self.today.strftime("%H:%M"))
        self.months = ['January', 'February', 'March', 'April',
                       'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.weekday = self.weekdays[calendar.weekday(self.year, self.month, self.day)]
        print(self.today)
        print('День: ',self.day)
        print("Месяц: ",self.months[self.month-1])
        print('День недели: ', self.weekday)
        print("Время: ",self.time)



TodayDateTime()