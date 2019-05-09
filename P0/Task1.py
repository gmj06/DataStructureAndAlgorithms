"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('Udacity/DatastructureAndAlgorithms/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('Udacity/DatastructureAndAlgorithms/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_telephone_numbers = set()

for text in texts:
    unique_telephone_numbers.add(text[0])
    unique_telephone_numbers.add(text[1])

for call in calls:
    unique_telephone_numbers.add(call[0])
    unique_telephone_numbers.add(call[1])

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")
