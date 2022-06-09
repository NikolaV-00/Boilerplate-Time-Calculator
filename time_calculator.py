def add_time(start, duration, day=''):
    extra_minutes = 0
    extra_hours = 0
    extra_days = 0
    final_ampm = ''
    final_day = ''

    # split the start string into hours, minutes and AM/PM
    # hours will be before ':'
    # minutes between ':' and the blank space after
    # AM/PM will be last two characters
    find_colon_start = start.find(':')
    space_start = start.find(' ')

    start_hours = start[:find_colon_start]
    start_minutes = start[find_colon_start + 1:find_colon_start + 3]
    start_ampm = start[space_start + 1:]

    # split duration string into hours and minutes
    # hours come before ':'
    # minutes after ':' character
    find_colon_duration = duration.find(':')

    duration_hours = duration[:find_colon_duration]
    duration_minutes = duration[find_colon_duration + 1:]

    # check if the hours and minutes contain any characters
    # other than digits
    try:
        float_start_hours = float(start_hours)
        float_start_minutes = float(start_minutes)
        float_duration_hours = float(duration_hours)
        float_duration_minutes = float(duration_minutes)
    except ValueError:
        return "Error: Time (hh:mm) must contain only digits"

    # translate 12-hour clock to 24-hour clock
    if start_ampm == "PM":
        float_start_hours += 12

    # minutes after adding duration values to start values
    final_minutes = float_start_minutes + float_duration_minutes
    # if minutes are >= to 60,
    # modulus will calculate the new value of minutes
    # and floor division will calculate extra hours
    if final_minutes >= 60:
        extra_hours = final_minutes // 60
        final_minutes = final_minutes % 60
    # print(extra_hours, final_minutes)

    # hours after adding duration values, start values and
    # extra hours from excess minutes
    final_hours = float_start_hours + float_duration_hours + extra_hours
    # if hours are >= to 24,
    # modulus will calculate new value of hours
    # and floor division will calculate extra days
    # in case they are required
    if final_hours >= 24:
        extra_days = int(final_hours // 24)
        final_hours = final_hours % 24

    # translate 24-hour clock to 12-hour clock
    # 13:00 will be translated to 1:00 PM
    if final_hours <= 11 and final_minutes <= 59:
        final_ampm = "AM"
    elif final_hours == 12:
        final_ampm = "PM"
    else:
        final_hours -= 12
        final_ampm = "PM"
    # 00:00 in 24-hour clock is 12:00 AM in 12-hour clock
    if final_hours == 0:
        final_hours = 12

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # find the index position of the day,
    # if the day is mentioned
    # day.capitalize() will capitalize
    # the first letter of the day
    # case sensitivity does not matter on input
    day = day.capitalize()
    if day != '':
        day_position = days.index(day)

        # find the day index of the day after adding
        # any potential days from calculating hours
        final_day_position = day_position + extra_days
        if final_day_position > 7:
            final_day_position = final_day_position % 7
        final_day_position = int(final_day_position)

        final_day = days[final_day_position]

    final_minutestr = str(int(final_minutes))
    final_hourstr = str(int(final_hours))

    if len(final_minutestr) < 2:
        final_minutestr = '0' + final_minutestr

    final_time = final_hourstr + ':' + final_minutestr

    if extra_days == 1:
        extra_days_line = "(next day)"
    elif extra_days > 1:
        extra_days_line = '(' + str(extra_days) + ' days later)'
    else:
        extra_days_line = ''

    if day != '':
        if extra_days_line != '':
            new_time = final_time + " " + final_ampm + ', ' + final_day + ' ' + extra_days_line
        else:
            new_time = final_time + " " + final_ampm + ', ' + final_day
    else:
        if extra_days_line != '':
            new_time = final_time + ' ' + final_ampm + ' ' + extra_days_line
        else:
            new_time = final_time + ' ' + final_ampm

    return new_time