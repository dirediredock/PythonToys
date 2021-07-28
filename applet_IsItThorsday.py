
# by Matias I. Bofarull Oddo - July 21st 2021

import datetime

thisMoment = datetime.datetime.now()

Hour = thisMoment.hour
Minute = thisMoment.minute
Second = thisMoment.second

# In Python datetime index 0 is Monday.

Weekday = datetime.datetime.today().weekday() - 3

if Weekday == 0:
    print("Holy Fuck today is Thorsday !!!")
else:
    print("Sadly, today is not the Thorsday. Go nap until it is.")

    if Weekday == -3:
        Day = 2
    if Weekday == -2:
        Day = 1
    if Weekday == -1:
        Day = 0
    if Weekday == +1:
        Day = 5
    if Weekday == +2:
        Day = 4
    if Weekday == +3:
        Day = 3

    totalHours = Day*24 + 23-Hour

    if totalHours != 1:
        stringHours = totalHours, " hours"
    else:
        stringHours = totalHours, " hour"

    totalMinutes = 59-Minute

    if totalMinutes != 1:
        stringMinutes = totalMinutes, " minutes"
    else:
        stringMinutes = totalMinutes, " minute"

    totalSeconds = 60-Second

    if totalSeconds != 1:
        stringSeconds = totalSeconds, " seconds"
    else:
        stringSeconds = totalSeconds, " second"

    # Here be tuples converted into strings.

    delimiter = ''

    A = stringHours
    stringHours = delimiter.join([str(A) for A in A])

    A = stringMinutes
    stringMinutes = delimiter.join([str(A) for A in A])

    A = stringSeconds
    stringSeconds = delimiter.join([str(A) for A in A])

    # Here be string concatenation.

    print("Nap time required: " +
          stringHours + ", " +
          stringMinutes + ", and " +
          stringSeconds + ".")
