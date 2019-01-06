""" __doc__ """

# define lambda for readability
RTN = lambda: '\n'

# populate dictionary
AGILE_MANIFESTO_DICT = {
    'people and interactions': 'processes and tools',
    'working software': 'comprehensive documentation',
    'customer collaboration': 'contract negotiation',
    'responding to change': 'following a plan',
}

# announce topic
print RTN()
print "agile manifesto".upper()

# loop through dictionary and prompt user for the b sections in the response to a sections
for k, v in AGILE_MANIFESTO_DICT.items():
    print "%s" % (k)
    prompt_user = raw_input("over\n")
    if prompt_user == v:
        print "correct"
    else:
        print "incorrect"
    print RTN()
