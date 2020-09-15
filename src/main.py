import datetime
from course import Course
import quarter
import tokens

classes = [Course("CSE 11", datetime.time(hour=14, minute=0), datetime.time(hour=16, minute=0), ["M", "W", "F"]),
           Course("Math 20C", datetime.time(hour=17), datetime.time(hour=18), ["M", "W", "F"])]
q = quarter.Quarter(datetime.date(month=9, day=12, year= 2020), datetime.date(month=10, day=19, year= 2020), classes)
# q.get_all_meetings()
# print(classes[0].get_notion_dates())
q.add_to_notion(tokens.token_v2, tokens.url)


