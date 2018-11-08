rtn = lambda: '\n'

protocols = {
    'HTTP': 'application',
    'FTP': 'application',
    'LPD': 'application',
    'SMTP': 'application',
    'Telnet': 'application',
    'TFTP': 'application',
    'EDI': 'application',
    'POP3': 'application',
    'IMAP': 'application',
    'SNMP': 'application',
    'NNTP': 'application',
    'S-RPC': 'application',
    'SET': 'application',
    'ASCII': 'presentation',
    'EBCDICM': 'presentation',
    'TIFF': 'presentation',
    'JPEG': 'presentation',
    'MPEG': 'presentation',
    'MIDI': 'presentation',
    'TCP': 'transport',
    'UDP': 'transport',
    'SPX': 'transport',
    'SSL': 'transport',
    'TLS': 'transport',
    'ICMP': 'network',
    'RIP': 'network',
    'OSPF': 'network',
    'BGP': 'network',
    'IGMP': 'network',
    'IP': 'network',
    'IPSec': 'network',
    'IPX': 'network',
    'NAT': 'network',
    'SKIP': 'network',
    'SLIP': 'data link',
    'PPP': 'data link',
    'ARP': 'data link',
    'RARP': 'data link',
    'L2F': 'data link',
    'L2TP': 'data link',
    'PPTP': 'data link',
    'ISDN': 'data link',
    'EIA/TIA-232 and EIA/TIA-449': 'physical',
    'X.21': 'physical',
    'HSSI': 'physical',
    'SONET': 'physical',
    'V.24 and V.35': 'physical',
}

# print(len(protocols))

# create list to be populated later
incorrects = []

# quiz user
for k, v in protocols.items():
    print("%s") % (k)
    which_layer = raw_input("which layer ")
    if which_layer == v:
        print("correct")
    else:
        print("Incorrect. The correct answer is %s") % (v)
        incorrects.append(k)
    print(rtn())

# results
if len(incorrects) > 0:
    print("items to review".upper())
    for protocol in incorrects:
        print(protocol)
else:
    print("100%! Great job!!!")

# for readability
print(rtn())