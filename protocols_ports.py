""" __doc__ """

# for readability
RTN = lambda: "\n"

# header
print "protocols and ports".upper()

# build dictionary
PROTOCOLS_PORTS_DICT = {
    'FTP': '21',
    'SSH': '22',
    'Telnet': '23',
    'SMTP': '25',
    'DNS': '53',
    'TFTP': '69',
    'HTTP': '80',
    'POP3': '110',
    'NTP': '123',
    'SSL': '443',
    'LPD': '515',
    'Microsoft SQL Server': '1433',
    'Oracle': '1521',
    'H.323': '1720',
    'PPTP': '1723',
    'RDP': '3389',
    }

# create list to be populated later
INCORRECTS = []

# quiz user
for k, v in PROTOCOLS_PORTS_DICT.items():
    print "protocol %s" % (k)
    port_answer = raw_input("port ")
    if port_answer == v:
        print "correct"
    else:
        print "incorrect"
        print "the correct answer is %s" % (v)
        INCORRECTS.append(k)
    print RTN()

# results - show user what needs review
if len(INCORRECTS) > 0:
    print "items for review".upper()
    for protocol in INCORRECTS:
        print protocol
else:
    print "100%! Great job!!!"

# for readability
print RTN()
