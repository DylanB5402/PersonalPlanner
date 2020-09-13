import datetime
import course

class Quarter:

    def __init__(self, start_date : datetime.date, end_date : datetime.date, course_list : list):
        self.start_date = start_date
        self.end_date = end_date

    def get_all_meetings(self):
        pass
