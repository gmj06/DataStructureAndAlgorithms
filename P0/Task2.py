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
max_telephone_no = ''
telephone_no_dict = {}

for i, call in enumerate(calls):
    if (call[0] in telephone_no_dict):
        telephone_no_dict[call[0]] += int(call[3])
    else:
        telephone_no_dict[call[0]] = int(call[3])
    
    if (call[1] in telephone_no_dict):
        telephone_no_dict[call[1]] += int(call[3])
    else:
        telephone_no_dict[call[1]] = int(call[3])

    if(telephone_no_dict[call[0]] > max_time_on_phone):
        max_time_on_phone = telephone_no_dict[call[0]]
        max_telephone_no = call[0]

    if(telephone_no_dict[call[1]] > max_time_on_phone):
        max_time_on_phone = telephone_no_dict[call[1]]
        max_telephone_no = call[1]

print(f"{max_telephone_no} spent the longest time, {max_time_on_phone} seconds, on the phone during September 2016.")




