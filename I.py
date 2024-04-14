def choose_days(N, year, holidays, first_day_of_year):
    def is_leap_year(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    def day_of_week(day, month, year):
        months = {
            'January': 0, 'February': 31, 'March': 59, 'April': 90, 'May': 120,
            'June': 151, 'July': 181, 'August': 212, 'September': 243, 'October': 273,
            'November': 304, 'December': 334
        }
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        total_days = day + months[month]
        if is_leap_year(year) and month in ['February', 'March']:
            total_days += 1
        return days[(year - 1 + total_days) % 7]

    work_days = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    for day in range(1, 367):
        current_day = day_of_week(day, 'January', year)
        if current_day not in work_days:
            continue
        if current_day == first_day_of_year:
            current_day_is_holiday = True
        else:
            current_day_is_holiday = False
        for holiday in holidays:
            if day == holiday[0] and current_day == day_of_week(holiday[0], holiday[1], year):
                current_day_is_holiday = True
        if not current_day_is_holiday:
            work_days[current_day] += 1

    best_day = max(work_days, key=work_days.get)
    worst_day = min(work_days, key=work_days.get)

    return best_day, worst_day


N = int(input())
year = int(input())
holidays = []
for _ in range(N):
    day, month = input().split()
    holidays.append((int(day), month))
first_day_of_year = input().strip()

best_day, worst_day = choose_days(N, year, holidays, first_day_of_year)
print(best_day, worst_day)

