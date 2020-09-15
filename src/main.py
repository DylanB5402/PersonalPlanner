import datetime
from course import Course
import quarter
import tokens

classes = [Course("CSE 20 Lecture", datetime.time(hour=8, minute=0), datetime.time(hour=8, minute=50), ["M", "W", "F"]),
           Course("CSE 20 Discussion", datetime.time(hour=13, minute=0), datetime.time(hour=13, minute=50), ["M"]),
           Course("Math 20C Lecture", datetime.time(hour=9, minute=0), datetime.time(hour=9, minute=50), ["M", "W", "F"]),
           Course("Math 20C Discussion", datetime.time(hour=17), datetime.time(hour=17, minute=50), ["M"]),
           Course("CSE 11 Lecture", datetime.time(hour=10, minute=0), datetime.time(hour=10, minute=50), ["M", "W", "F"]),
           Course("CSE 11 Discussion", datetime.time(hour=8, minute=0), datetime.time(hour=8, minute=50), ["T"]),
           Course("WCWP 10A", datetime.time(hour=17, minute=0), datetime.time(hour=18, minute=20), ["T", "Th"]),

           ]

q = quarter.Quarter(datetime.date(month=10, day=1, year= 2020), datetime.date(month=12, day=11, year= 2020), classes)
# q.get_all_meetings()
# print(classes[0].get_notion_dates())
q.add_to_notion(tokens.token_v2, tokens.url)


