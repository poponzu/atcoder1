import math

y = int(input())
m = int(input())
d = int(input())


def count_days(year, month, day):
    if month == 1:
        year -= 1
        month = 13

    if month == 2:
        year -= 1
        month = 14

    day_count = 365 * year + year // 4 - year // 100 + year // 400 + (
                (306 * (month + 1)) // 10) + day

    return day_count


today = count_days(2014,5,17)
target = count_days(y,m,d)

print(today - target)
