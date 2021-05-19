"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)

    # List of list elements containing all calls
    texts = list(reader)

    # Access the first element in the list
    first_record = texts[0]
    income_number = first_record[0]
    answering_number = first_record[1]
    timestamp = first_record[2]

    # Output the result
    print(f'First record of texts, {income_number} texts {answering_number} at time {timestamp}')


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # Access the last element in the list
    last_record = calls[-1]
    income_number = last_record[0]
    answering_number = last_record[1]
    timestamp = last_record[2]
    lasting = last_record[3]

    # Output result
    print(f'Last record of calls, {income_number} calls {answering_number} at time {timestamp}, lasting {lasting} seconds')


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

