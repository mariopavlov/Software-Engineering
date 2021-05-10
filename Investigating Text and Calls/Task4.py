"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import telephones


# Set to store all caller telemarketer numbers
callers = set()

# Set of Phone numbers that are extracted from
# Outgoing calls, sending text and receiving texts
non_telemarketers = set()


# Pass through texts.csv file and look for telemarketers numbers
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        sender = text[0]
        receiver = text[1]

        non_telemarketers.add(sender)
        non_telemarketers.add(receiver)


# Pass through calls.csv and look for telemarketers numbers
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        caller = call[0]
        receiver = call[1]

        callers.add(caller)
        non_telemarketers.add(receiver)

# Look for telemarketers
telemarketers = callers.difference(non_telemarketers)

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

