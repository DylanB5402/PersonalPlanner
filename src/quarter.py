import datetime
import course
from notion.client import NotionClient
from notion.collection import NotionDate

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
                        # c.meeting_dates.append(datetime.datetime.combine(date, c.time))
                        c.meeting_dates.append(date)
            date += datetime.timedelta(days=1)

    def add_to_notion(self, notion_token_v2 : str, notion_url : str):
        client = NotionClient(token_v2=notion_token_v2)
        cv = client.get_collection_view(notion_url)
        self.get_all_meetings()
        for c in self.course_list:
            for date in c.get_notion_dates():
                row = cv.collection.add_row()
                row.Class = c.name
                row.Date = date

