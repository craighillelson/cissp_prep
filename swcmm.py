""" __doc__ """

# for readability
RTN = lambda: '\n'

# swcmm dictionary
SWCMM = [
    'initial',
    'repeatable',
    'defined',
    'managed',
    'optimized',
    ]

i = 0

# quiz user
for item in SWCMM:
    prompt_user = raw_input("name one of the elements ")
    if prompt_user == SWCMM[i]:
        print "correct"
        print RTN()
    else:
        print "Incorrect. The correct answer is %s" % (SWCMM[i])
        print RTN()
    i = i + 1
