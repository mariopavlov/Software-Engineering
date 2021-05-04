"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    longest_call = 0
    telephone_number = ''

    for call in calls:
        call_duration = int(call[3])

        if call_duration > longest_call:
            longest_call = call_duration
            telephone_number = call[0]

    print(f'{telephone_number} spent the longest time, {longest_call} seconds, on the phone during September 2016.')


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

