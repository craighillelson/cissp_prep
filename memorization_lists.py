# imports
from lists import *
import functions

# prompt user
# validate user input
print(functions.rtn())
print("categories".upper())

# categories
for k, v in sorted(choices.iteritems(), key=lambda (k,v): (k,v)):
	print("%s %s") % (k, v)

print(functions.rtn())

# ask user which category they'd like to drill
topic = raw_input("What would you like to drill? ")

# remove that category from the list and ask the user if they'd like to drill one of the remaining categories

# run functions
value = functions.choice_switch(topic)
a = functions.value_switch(value)

# loop through list, ask user to name all of them items in lst
# if user answers correctly, add that answer to the corrects list and remove same from lst
# if user answers incorrectly, add that answer to the incorrects list and remove same from lst
functions.quiz(a)

# for readability
print(functions.rtn())

lst = set(a) - set(corrects)

# results logic
if len(lst) < 1:
	print("100%!!! Great job!")
elif len(lst) < 2:
	print("item for review".upper())
	for item in lst:
		print(item)
else:
	print("items for review".upper())
	for item in lst:
		print(item)	

# write results to a file
print(functions.rtn())