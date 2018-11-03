# for readability
rtn = lambda: '\n'

# header
print("protocols and ports".upper())

# build dictionary
protocols_ports_dict = {
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
	'RDP': '3389',
}

# create list to be populated later
incorrects = []

# quiz user
for k, v in protocols_ports_dict.items():
	print("protocol %s") % (k)
	port_answer = raw_input("port ")
	if port_answer == v:
		print("correct")
	else:
		print("incorrect")
		print("the correct answer is %s") % (v)
		incorrects.append(k)
	print(rtn())

# show user what needs review
print("items for review".upper())
for protocol in incorrects:
	print(protocol)