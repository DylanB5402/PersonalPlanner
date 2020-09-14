import datetime
import utils
from notion.collection import NotionDate

# 0 = monday, 1 = tues, 2 = wed, 3 = thurs, 4, = fri, 5 = sat, 6 = sunday
class Course:

    def __init__(self, name : str, time : datetime.time, meeting_days : list):
        self.name = name
        self.time = time
        self.meeting_days = utils.meeting_days_to_numbers(meeting_days)
        self.meeting_dates = []

    def get_notion_dates(self):
        notion_dates = []
        for date in self.meeting_dates:
            notion_dates.append(NotionDate(date))
        return notion_dates


