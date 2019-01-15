""" __doc__ """

# for readability
RTN = lambda: '\n'

# header
print "fire suppression systems".upper()

# build dictionary
water_suppression_systems_dict = {
    'wet pipe': 'full of water',
    'dry pipe': 'fills with water',
    'deluge': 'dry pipe with bigger pipes',
    'preaction': 'fills when the early stages of a fire are detected',
    }

# create list to be populated later
incorrects = []

# quiz user
for k, v in water_suppression_systems_dict.items():
    print "suppression system: %s" % (k)
    definition = raw_input("definition: ")
    if definition == v:
        print "correct"
    else:
        print "incorrect"
        print "the correct answer is %s" % (v)
        incorrects.append(k)
    print RTN()

# results - show user what needs review
if incorrects > 0:
    print "items for review".upper()
    for suppression_system in incorrects:
        print suppression_system
else:
    print "100%! Great job!!!"

# for readability
print RTN()
