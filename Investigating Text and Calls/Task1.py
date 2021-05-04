"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_number = set()


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        unique_number.add(text[0])
        unique_number.add(text[1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        unique_number.add(call[0])
        unique_number.add(call[1])


# At this point we are ready with counting, and I need to print output
un_len = len(unique_number)
print(f'There are {un_len} different telephone numbers in the records.')

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
