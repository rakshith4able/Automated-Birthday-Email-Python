##################### Automated Birthday Wishing Email Project ######################
import datetime as dt

# TODO 1 Starting files => 1)main.py 2)3 random letter templates 3)birthdays.csv containing name,email,birthday entries

# TODO 2 get current date and time and check if today matches a birthday in the birthdays.csv for every entry
now=dt.datetime.now()
month=now.month
day=now.day


# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from
#  birthdays.csv Send the letter generated to that person's email address.
