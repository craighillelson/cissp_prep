# for readability
rtn = lambda: '\n'

# swcmm dictionary
swcmm = [
    'initial',
    'repeatable',
    'defined',
    'managed',
    'optimized',
    ]

i = 0

# quiz user
for item in swcmm:
    prompt_user = raw_input("name one of the elements ")
    if prompt_user == swcmm[i]:
        print("correct")
        print(rtn())
    else:
        print("Incorrect. The correct answer is %s") % (swcmm[i])
        print(rtn())
    i = i + 1