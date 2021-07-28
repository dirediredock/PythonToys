# THE BIRTHDAY PARADOX

# The Birthday Paradox is not really a paradox, but the unintuitively
# high probability of two people sharing a birthday within a relatively
# small group. Here an arbitrary number of random birthdays are generated
# and compared for matches, and a match rate is calculated.

import datetime
import random

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

numberOfPeople = 42

birthdays = []
matching = []

print('\nLIST OF {} BIRTHDAYS\n'.format(numberOfPeople))

for i in range(numberOfPeople):

    startOfYear = datetime.date(1, 1, 1)
    randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
    birthday = startOfYear + randomNumberOfDays
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText)
    birthdays.append(birthday)

print('\nLIST OF MATCHING BIRTHDAYS\n')

if len(birthdays) == len(set(birthdays)):
    print('All birthdays are unique.')
else:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                monthName = MONTHS[birthdayA.month - 1]
                dateText = '{} {}'.format(monthName, birthdayA.day)
                print(dateText)
                matching.append(birthdayA)

matchPercent = len(matching)/numberOfPeople * 100

if len(matching) != 1:
    print('\nThere are {} matching birthdays '.format(len(matching)) +
          'out of {}, '.format(numberOfPeople) +
          'or a {}% match rate.\n'.format(int(matchPercent)))
else:
    print('\nThere is 1 matching birthday ' +
          'out of {}, '.format(numberOfPeople) +
          'or a {}% match rate.\n'.format(int(matchPercent)))
