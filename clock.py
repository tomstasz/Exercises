def timeConv(s):
    time_split = s.split(':')
    print('time_split:', time_split)
    hour = int(time_split[0])
    if 'P' in time_split[2] and hour != 12:
        hour += 12
    elif 'A' in time_split[2] and hour == 12:
        hour = '00'
    elif 'A' in time_split[2] and hour < 10:
        hour = "0{}".format(hour)

    sec = time_split[2][:2]

    res = "{}:{}:{}".format(hour, time_split[1], sec)

    print(res)

    return res


timeConv("07:05:45PM")
timeConv("12:40:22AM")
timeConv("06:40:03AM")
timeConv("04:59:59AM")