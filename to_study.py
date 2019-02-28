""" __doc__ """

import csv
from collections import namedtuple

# for readability
RTN = lambda: "\n"

# define function
def choice_to_file(topic):
    """ swtich """
    switcher = {
        "a": "FORMULAS",
        # "b": "protocols_ports.py",
        # "c": "ports_protocols.py",
        # "d": "symmetric_memorization_chart.py",
        # "e": "hash_algorithm_memorization_chart.py",
        # "f": "network_cabling_types.py",
        # "g": "name_that_layer.py",
        # "h": "ideal.py",
        # "i": "mnemonics.py",
        # "j": "swcmm.py",
        # "k": "water_suppression_systems.py",
        }
    return switcher.get(topic, "nothing")

# offer the user some choices of lists to drill
USER_CHOICE = input(
    "What would you like to study?\n"
    "a. formulas\n"
    # "b. protocols and ports\n"
    # "c. ports and protocols\n"
    # "d. symmetric memorization chart\n"
    # "e. hash algorithm memorization chart\n"
    # "f. network cabling types\n"
    # "g. which layer?\n"
    # "h. ideal\n"
    # "i. mnemonics\n"
    # "j. swcmm\n"
    # "k. water suppression systems\n"
    )

print(RTN())
print(f"You chose {choice_to_file(USER_CHOICE)}")
print(RTN())
# run function an load the file of the user's choice
# TOPIC_TO_MEM = choice_to_file(USER_CHOICE)
# execfile(TOPIC_TO_MEM)

# header
# print(USER_CHOICE.upper())
print(choice_to_file(USER_CHOICE))
USER_CHOICE_CSV = choice_to_file(USER_CHOICE).lower()+".csv"
# print(USER_CHOICE_CSV)
USER_CHOICE_DCT = choice_to_file(USER_CHOICE)+"_DCT"
USER_CHOICE_DCT = {}
# print(USER_CHOICE_DCT)


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
        # include try statement to catch user error
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
