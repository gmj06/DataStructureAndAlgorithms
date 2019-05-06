"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import math

with open('Udacity/DatastructureAndAlgorithms/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('Udacity/DatastructureAndAlgorithms/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
area_code_mobile_prefix_list = set()
fixed_line_Bangalore_call_count = 0
total_Bangalore_call_count = 0

for call in calls:
  answering_code = ""

  if(call[0][:5] == "(080)"):
    total_Bangalore_call_count += 1

    if (call[1][:5] == "(080)"):
      fixed_line_Bangalore_call_count += 1

    if (call[1][:3] == "140"):
      answering_code = call[1][:3]
    elif (call[1][:1] == "("):
      start_index = call[1].find("(")
      end_index = call[1].find(")")
      answering_code = call[1][:end_index - start_index + 1] 
    else:
      answering_code = call[1][:4]
  
  if (answering_code != ""):
    area_code_mobile_prefix_list.add(answering_code)
    
new_area_code_list = list(area_code_mobile_prefix_list)
new_area_code_list.sort()

for code in new_area_code_list:
  print(code)


percentage_fixed_line_bangalore_call = (fixed_line_Bangalore_call_count/total_Bangalore_call_count) * 100
percentage_2_decimals = math.floor(percentage_fixed_line_bangalore_call * 100 + 0.5)/100

print(f"{percentage_2_decimals} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
