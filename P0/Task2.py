"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('Udacity/DatastructureAndAlgorithms/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('Udacity/DatastructureAndAlgorithms/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max_time_on_phone = -1
max_index = -1

for i, call in enumerate(calls):
    if(int(call[3]) > max_time_on_phone):
        max_time_on_phone = int(call[3])
        max_index = i

print(f"{calls[max_index][0]} spent the longest time, {calls[max_index][3]} seconds, on the phone during September 2016.")
print(f"{calls[max_index][1]} spent the longest time, {calls[max_index][3]} seconds, on the phone during September 2016.")




