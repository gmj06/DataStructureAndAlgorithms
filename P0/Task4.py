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

text_sender = set()
text_receiver = set()
call_receiver = set()
call_sender_marketing = set()

for text in texts:
    text_sender.add(text[0])
    text_receiver.add(text[1])

for call in calls:
    call_receiver.add(call[1])
    if (call[0][:3] == "140" and call[0] not in text_sender and call[0] not in text_receiver):
        call_sender_marketing.add(call[0])
    
call_sender_marketing_final = list(call_sender_marketing - call_receiver)
call_sender_marketing_final.sort()                

print("These numbers could be telemarketers: ")
for caller in call_sender_marketing_final:
    print(caller)