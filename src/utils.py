import datetime


# 0 = monday, 1 = tues, 2 = wed, 3 = thurs, 4, = fri, 5 = sat, 6 = sunday
def meeting_days_to_numbers(days : list):
    out = []
    for day in days:
        if day == 'M':
            out.append(0)
        elif day == 'T':
            out.append(1)
        elif day == 'W':
            out.append(2)
        elif day == 'Th':
            out.append(3)
        elif day == 'F':
            out.append(4)
    return out
