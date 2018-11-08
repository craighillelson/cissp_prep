# for readability
rtn = lambda: '\n'

# header
print("protocols and ports".upper())

# build dictionary
protocols_ports_dict = {
    '21': 'FTP',
    '22': 'SSH',
    '23': 'Telnet',
    '25': 'SMTP',
    '53': 'DNS',
    '69': 'TFTP',
    '80': 'HTTP',
    '110': 'POP3',
    '123': 'NTP',
    '443': 'SSL',
    '515': 'LPD',
    '1433': 'Microsoft SQL Server',
    '1521': 'Oracle',
    '1720': 'H.323',
    '1723': 'PPTP',
    '3389': 'RDP',
}

# create list to be populated later
incorrects = []

# quiz user
for k, v in protocols_ports_dict.items():
    print("port %s") % (k)
    port_answer = raw_input("protocol ")
    if port_answer == v:
        print("correct")
    else:
        print("incorrect")
        print("the correct answer is %s") % (v)
        incorrects.append(k)
    print(rtn())

# results - show user what needs review
if len(incorrects) > 0:
    print("items for review".upper())
    for port in incorrects:
        print(port)
else:
    print("100%! Great job!!!")

# for readability
print(rtn())