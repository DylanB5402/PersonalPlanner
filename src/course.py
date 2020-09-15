import datetime
import utils
from notion.collection import NotionDate


# 0 = monday, 1 = tues, 2 = wed, 3 = thurs, 4, = fri, 5 = sat, 6 = sunday
class Course:

    def __init__(self, name : str, time : datetime.time, end_time :datetime.time, meeting_days : list):
        self.name = name
        self.time = time
        self.end_time = end_time
        self.meeting_days = utils.meeting_days_to_numbers(meeting_days)
        self.meeting_dates = []

    def get_notion_dates(self):
        notion_dates = []
        for date in self.meeting_dates:
            notion_dates.append(NotionDate(start=datetime.datetime.combine(date, self.time), end=datetime.datetime.combine(date, self.end_time)))
        return notion_dates


