""" __doc__ """

# for readability
RTN = lambda: '\n'

# header
print "formulas".upper()

# build dictionary
FORMULAS = {
    'exposure factor': '%',
    'sle': 'av * ef',
    'aro': '# / year',
    'ale': 'sle * aro or av * ef * aro',
    'acs': '$ / year',
    'value of acs': '(ale1 - ale2) - acs',
    }

# create list to be populated later
INCORRECTS = []

# readability
print RTN()

# quiz user
for k, v in FORMULAS.items():
    user_answer = raw_input(k+" ")
    if user_answer == v:
        print "correct"
    else:
        see_answer = raw_input(
            "Incorrect. Would you like to see the correct answer? "
            )
        INCORRECTS.append(k)
        if see_answer == 'yes':
            print v
        else:
            pass
    print RTN()

# show user what needs review
if INCORRECTS:
    print "items for review".upper()
    for item in INCORRECTS:
        print item
else:
    print "100%! Great job!!!"

# for readability
print RTN()
