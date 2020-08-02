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
        self.data_numbers = 434
        
        
        self.real_time = self.create_time_bar()
        
    
    def create_time_bar(self):
        leap_years = leap_year(self.year_start)
        real_time = []
        for i in range(self.data_numbers):
            self.minute_start = self.minute_start + 10
            if self.minute_start % 60 == 0:
                self.minute_start = 0
                self.hour_start = self.hour_start + 1
                if self.hour_start % 24 == 0:
                    self.hour_start = 0
                    self.day_start = self.day_start + 1
                    if leap_year and self.year_start % 2 == 0 :
                        if self.day_start % 30 == 0:
                            self.day_start = 1
                            self.month_start += 1 
                    elif leap_year == False and self.year_start %2 == 0:
                        if self.day_start % 29 == 0:
                            self.day_start = 1
                            self.month_start += 1 
                    elif self.year_start % 1 == 0 or self.year_start % 3 == 0 or self.year_start % 5 == 0 or self.year_start % 7 == 0 or \
                        self.year_start % 8 == 0 or self.year_start % 10 == 0 or self.year_start % 12 == 0 :
                         if self.day_start % 32 == 0:
                                self.day_start = 1
                                self.month_start += 1 
                    else:
                         if self.day_start % 31 == 0:
                                self.day_start = 1
                                self.month_start += 1 

            if self.minute_start < 10: minutes_time = "0"+str(self.minute_start)
            else: minutes_time = str(self.minute_start)
            
            if self.hour_start < 10: hour_time = "0"+str(self.hour_start)
            else: hour_time = str(self.hour_start)

            if self.month_start < 10: month_time = "0"+str(self.month_start)
            else: month_time = str(self.month_start)

            if self.day_start < 10: day_time = "0"+str(self.day_start)
            else: day_time = str(self.day_start)
               
            starttimes = str(self.year_start) + "-" + month_time + "-" + day_time + "-" + hour_time + "-" + minutes_time
            real_time.append(starttimes)
        return real_time
