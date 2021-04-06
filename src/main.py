import datetime
from course import Course
import quarter
import tokens

# classes = [Course("CSE 20 Lecture", datetime.time(hour=8, minute=0), datetime.time(hour=8, minute=50), ["M", "W", "F"]),
#            Course("CSE 20 Discussion", datetime.time(hour=13, minute=0), datetime.time(hour=13, minute=50), ["M"]),
#            Course("Math 20C Lecture", datetime.time(hour=9, minute=0), datetime.time(hour=9, minute=50), ["M", "W", "F"]),
#            Course("Math 20C Discussion", datetime.time(hour=17), datetime.time(hour=17, minute=50), ["M"]),
#            Course("CSE 11 Lecture", datetime.time(hour=10, minute=0), datetime.time(hour=10, minute=50), ["M", "W", "F"]),
#            Course("CSE 11 Discussion", datetime.time(hour=8, minute=0), datetime.time(hour=8, minute=50), ["T"]),
#            Course("WCWP 10A", datetime.time(hour=17, minute=0), datetime.time(hour=18, minute=20), ["T", "Th"]),
#            ]

# classes = [Course("CSE 20 Lecture", datetime.time(hour=11, minute=0), datetime.time(hour=11, minute=50), ["M", "W", "F"]),
#            Course("CSE 20 Discussion", datetime.time(hour=11, minute=0), datetime.time(hour=11  , minute=50), ["T"]),
#            ]

# classes = [
    # Course("Math 18 Lecture", datetime.time(hour=10, minute=0), datetime.time(hour=10, minute=50), ["M", "W", "F"]),
    # Course("CSE 12 Lecture", datetime.time(hour=11, minute=0), datetime.time(hour=11, minute=50), ["M", "W", "F"]),
    # Course("CSE 15L Lecture", datetime.time(hour=13, minute=0), datetime.time(hour=13, minute=50), ["M", "W"]),
    # Course("CSE 12 Discussion", datetime.time(hour=11, minute=0), datetime.time(hour=11, minute=50), ["T"]),
    # Course("WCWP 10B", datetime.time(hour=14, minute=0), datetime.time(hour=15, minute=20), ["T", "Th"]),
    # Course("CSE 15L Lab", datetime.time(hour=9, minute=0), datetime.time(hour=10, minute=50), ["Th"]),
    # Course("Math 18 Discussion", datetime.time(hour=11, minute=0), datetime.time(hour=11, minute=50), ["Th"]),
# ]

classes = [
    Course("COG 1 Lecture", datetime.time(hour=12), datetime.time(hour=12, minute=50), ["M", "W", "F"]),
    Course("CSE 21 Lecture", datetime.time(hour=11), datetime.time(hour=12, minute=20), ["T", "Th"]),
    Course("CSE 30 Lecture", datetime.time(hour=14), datetime.time(hour=15, minute=20), ["T", "Th"]),
    Course("LTCS 87", datetime.time(hour=11), datetime.time(hour=11, minute=50), ["W"]),
    Course("CSE 21 Discussion", datetime.time(hour=15), datetime.time(hour=15, minute=50), ["W"]),
    Course("CSE 30 Discussion", datetime.time(hour=11), datetime.time(hour=11, minute=45), ["F"] )
]

q = quarter.Quarter(datetime.date(month=3, day=29, year= 2021), datetime.date(month=6, day=4, year= 2021), classes)
# q.get_all_meetings()
# print(classes[0].get_notion_dates())
q.add_to_notion(tokens.token_v2, tokens.url)


