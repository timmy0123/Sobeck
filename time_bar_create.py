def leap_year(year):
    if year %4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else: return False
        else:
            return True
    else:
        return False






class time_bar():
    def __init__(self,year,month,day,hours,minutes):

        self.minute_start = minutes
        self.hour_start = hours
        self.day_start = day
        self.month_start = month
        self.year_start = year
        self.data_numbers = 433
        
        
        self.create_time_bar()
        
    
    def create_time_bar(self):
        leap_years = leap_year(int(year))
        real_time = []
        for i in self.data_numbers:
            self.minute_start = self.minute_start + 10
            if self.minute_start % 60 == 0:
                self.minute_start = 0
                self.hour_start = self.hour_start + 1
                if self.hour_start % 24 == 0:
                    self.hour_start = 0
                    self.day_start = self.day_start + 1
                    if leap_year and self.year_start % 2 == 0 :
                        if self.day_start % 29 == 0:
                            self.day_start = 1
                            self.month_start += 1 
                    elif leap_year == False and self.year_start %2 == 0:
                        if self.day_start % 28 == 0:
                            self.day_start = 1
                            self.month_start += 1 
                    elif self.year_start % 1 == 0 or self.year_start % 3 == 0 or self.year_start % 5 == 0 or self.year_start % 7 == 0 or \
                        self.year_start % 8 == 0 or self.year_start % 10 == 0 or self.year_start % 12 == 0 :
                         if self.day_start % 31 == 0:
                                self.day_start = 1
                                self.month_start += 1 
                    else:
                         if self.day_start % 30 == 0:
                                self.day_start = 1
                                self.month_start += 1 

            starttimes = str(self.year_start)+"-" + str(self.month_start) +str(day_start)+"-0"+str(hour_start)+"-0"+str(minute_start)
            if self.minute_start < 10: 
                if self.hour_start < 10:
                    if self.day_start < 10:
                        if self.month_start < 10:
                            starttimes = str(self.year_start) + "-0" + str(self.month_start) + "-0" + str(self.hour_start) + "-0" + str(self.minute_start)
                        else:
                            starttimes = str(self.year_start) + "-" + str(self.month_start) + "-0" + str(self.hour_start) + "-0" + str(self.minute_start)
                    else:
                         starttimes = str(self.year_start) + "-0" + str(self.month_start) + "-" + str(self.hour_start) + "-0" + str(self.minute_start)
                else:
                    starttimes = str(self.year_start) + "-" + str(self.month_start) + "-" + str(self.hour_start) + "-" + str(self.minute_start)
            else:starttimes = "2016-09-" +str(day_start)+"-"+str(hour_start)+"-"+str(minute_start)
            real_time.append(starttimes)
            return real_time
