""" __doc__ """

# imports
import dicts
import functions
from lists import *

def print_list():
    for item in LST:
        print item

# prompt user
# validate user input
print functions.rtn()
print "categories".upper()

# display categories
for k, v in sorted(dicts.categories.iteritems(), key=lambda (k, v): (k, v)):
    print "%s %s" % (k, v)

print functions.rtn()

# ask user which category they'd like to drill
TOPIC = raw_input("What would you like to drill? ")

# remove that category from the list and ask the user
# if they'd like to drill one of the remaining categories

# run functions
value = functions.choice_switch(TOPIC)
a = functions.value_switch(value)

print functions.rtn()
print "%s" % (value.upper())

# loop through list, ask user to name all of them items in LST
# if user answers correctly, add that answer to the corrects list and remove same from LST
# if user answers incorrectly, add that answer to the incorrects list and remove same from LST
functions.quiz(a)

# for readability
print functions.rtn()

percentage_correct = float(len(corrects)) / float(len(a))
LST = set(a) - set(corrects)

# results logic
if len(LST) < 1:
    print "100%!!! Great job!"
elif len(LST) < 2:
    print "You scored {0:.0%}".format(percentage_correct)
    print functions.rtn()
    print "item for review".upper()
    print_list()
else:
    print "You scored {0:.0%}".format(percentage_correct)
    print functions.rtn()
    print "items for review".upper()
    print_list()

# write results to a file
print functions.rtn()
