""" __doc__ """

# define lambda
RTN = lambda: '\n'

# define ideal list
IDEAL = [
    'initiating',
    'diagnosing',
    'establishing',
    'acting',
    'learning',
    ]

i = 0

# quiz user
for item in IDEAL:
    prompt_user = raw_input("name one of the elements ")
    if prompt_user == IDEAL[i]:
        print "correct"
        print RTN()
    else:
        print "Incorrect. The correct answer is %s" % (IDEAL[i])
        print RTN()
    i = i + 1
