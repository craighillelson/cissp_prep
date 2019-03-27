""" __doc__ """

import csv
from collections import namedtuple

# for readability
RTN = lambda: "\n"

# define function
def choice_to_file(topic):
    """ switch """
    switcher = {
        "a": "FORMULAS",
        "b": "PROTOCOLS_PORTS",
        "c": "PORTS_PROTOCOLS",
        "d": "802.11",
        # "e": "SYMMETRIC_MEMORIZATION_CHART",
        # "f": "network_cabling_types",
        # "g": "name_that_layer",
        # "h": "ideal",
        # "i": "mnemonics",
        # "j": "swcmm",
        # "k": "water_suppression_systems",
        # "l": "symmetric encryption block and key sizes",
        }
    return switcher.get(topic, "nothing")


# present user with categories
print(RTN())
print("categories\n".upper())
print("a: FORMULAS\nb: PROTOCOLS_PORTS\nc: PORTS_PROTOCOLS\n" \
      "d. 802.11")

# evaluate user's respponse
while True:
    USER_CHOICE = input("Please pick a category from the options above.\n"
                        ).lower().strip()
    if USER_CHOICE not in ['a', 'b', 'c', 'd']:
        print("invalid choice")
    else:
        break

print(RTN())
print(choice_to_file(USER_CHOICE))
USER_CHOICE_CSV = choice_to_file(USER_CHOICE).lower()+".csv"
USER_CHOICE_DCT = choice_to_file(USER_CHOICE)+"_DCT"
USER_CHOICE_DCT = {}

def open_csv(file, dct):
    """ open csv and populate a dictionary with its contents """
    with open(file) as csv_file:
        f_csv = csv.reader(csv_file)
        column_headings = next(f_csv)
        csv_row = namedtuple('Row', column_headings)
        for rows in f_csv:
            row = csv_row(*rows)
            dct[row.term] = row.definition


open_csv(f"csvs/{USER_CHOICE_CSV}", USER_CHOICE_DCT)

# create list to be populated later
INCORRECTS = []

# for readability
print(RTN())

# quiz user
for k, v in USER_CHOICE_DCT.items():
    user_answer = input(k+" ")
    if user_answer == v:
        print("correct")
        print(RTN())
    else:
        see_answer = input("Incorrect. Would you like to see the correct " \
                           "answer? (y/n) ")
        INCORRECTS.append(k)
        if see_answer == 'y':
            print(v)
        else:
            pass
        print(RTN())
print(RTN())

# show user what needs review
if INCORRECTS:
    print("items for review".upper())
    for item in INCORRECTS:
        print(item)
else:
    print("100%! Great job!!!")

# for readability
print(RTN())
