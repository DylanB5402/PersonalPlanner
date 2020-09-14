import datetime
import course

class Quarter:

    def __init__(self, start_date : datetime.date, end_date : datetime.date, course_list : list):
        self.start_date = start_date
        self.end_date = end_date
        self.course_list = course_list

    def get_all_meetings(self):
        date = self.start_date
        while date != self.end_date:
            if date.weekday() in [0, 1, 2, 3, 4]:
                for c in self.course_list:
                    if date.weekday() in c.meeting_days:
                        # print(date)
                        c.meeting_dates.append(datetime.datetime.combine(date, c.time))
                    print(c.meeting_dates)
            date += datetime.timedelta(days=1)

