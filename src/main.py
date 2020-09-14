import datetime
from course import Course
import quarter

classes = [Course("CSE 11", datetime.time(hour=14, minute=0), ["M", "W", "F"])]
q = quarter.Quarter(datetime.date(month=9, day=12, year= 2020), datetime.date(month=9, day=19, year= 2020), classes)
q.get_all_meetings()
print(classes[0].get_notion_dates())



