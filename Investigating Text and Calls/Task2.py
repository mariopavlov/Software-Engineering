"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import telephones


# I dont need to iterate over texts file for this task.
# So I can comment out the creation of the list
# with open('texts.csv', 'r') as f:
# reader = csv.reader(f)
# texts = list(reader)

phone_calls = {}


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        telephones.extract_duration(call, phone_calls)

# Finding maximum dict.value, and returning key for that value
    max_key = max(phone_calls, key=phone_calls.get)
    print(f'{max_key} spent the longest time,' +
          f' {phone_calls[max_key]} seconds, on the phone during September 2016.')

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

