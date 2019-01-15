""" __doc__ """

# define lambd and functions
RTN = lambda: "\n"

def correct():
    """ print correct """
    print "correct"

def incorrect():
    """ print incorrect """
    print "incorrect"

print RTN()

# build dictionary
SECURITY_MODES = {
    'dedicated': [
        'same',
        'none',
        'none',
        ],
    'system high': [
        'same',
        'yes',
        'none',
        ],
    'compartmented': [
        'same',
        'yes',
        'yes',
        ],
    'multilevel': [
        'different',
        'yes',
        'yes',
        ],
    }

# quiz user
for k, v in SECURITY_MODES.items():
    print "%s" % (k)
    print "%s, %s, %s" % (v[0], v[1], v[2])
    print RTN()
