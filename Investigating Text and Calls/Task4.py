"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import telephones


telemarketers = set()

# Set of Phone numbers that are extracted from
# Outgoing calls, sending text and receiving texts
non_telemarketers = set()


def find_non_telemarketers(data_list, is_texts):
    """ Iterating over calls and texts files looking for non-telemarketers """

    for item in data_list:
        # It is either sender or caller depending on the input
        sender = item[0]
        receiver = item[1]

        sender_type = telephones.get_telephone_type(sender)
        receiver_type = telephones.get_telephone_type(receiver)

        if is_texts and sender_type == 'telemarketers':
            non_telemarketers.add(sender)

        if receiver_type == 'telemarketers':
            non_telemarketers.add(receiver)


def filter_telemarketers(data_list):
    """ Iterate over calls file and filter out telemarketers """

    for call in data_list:
        caller_number = call[0]

        caller_type = telephones.get_telephone_type(caller_number)

        if caller_type == 'telemarketers':
            if caller_number not in non_telemarketers:
                telemarketers.add(caller_number)


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    find_non_telemarketers(texts, is_texts=True)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    find_non_telemarketers(calls, is_texts=False)
    filter_telemarketers(calls)


print('These numbers could be telemarketers: ')
for item in sorted(telemarketers):
    print(item)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

