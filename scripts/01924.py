# 2007/01/01 -> MON
x, y = map(int, input().split())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 0: 'SUN'}

days = 0
for i in range(x):
    days += days_in_month[i]

days += y
print(week.get(days % 7))


"""
# References
#   https://claude-u.tistory.com/23

import calendar
a, b = map(int, input().split())
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(day[calendar.weekday(2007,a,b)])
"""