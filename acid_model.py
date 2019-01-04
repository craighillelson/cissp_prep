""" __doc__ """

# define lambda for readability
RTN = lambda: '\n'

# populate dictionary
ACID = {
    'A': 'atomicity',
    'C': 'consistency',
    'I': 'isolation',
    'D': 'durability',
    }

ACID_LIST = []

# announce topic
print RTN()
print "acid".upper()

# loop through dictionary and prompt user for the b sections in the response to a sections
for k, v in ACID.items(): #sorted(acid_model.items()): #, key=lambda (k,v): (k,v)):
    prompt = "%s " % (k)
    prompt_user = raw_input(prompt)
    if prompt_user == v:
        print "correct"
    else:
        print "incorrect"
    print RTN()
