# define lambda and functions
rtn = lambda : '\n'

def choice_switch(a):
	switcher = {
		'a': 'osi layers',
		'b': 'firewalls',
		'c': 'bcp',
		'd': 'biometrics',
		'e': 'data link layer protocols',
		'f': 'session layer protocols',
		'g': 'security models',
		'h': 'ideal',
		'i': 'private sector classifications',
	}
	return switcher.get(a, 'none')

def value_switch(a):
	switcher = {
		'osi layers': osi,
		'firewalls': firewalls,
		'bcp': bcp,
		'biometrics': biometrics,
		'session layer protocols': session_layer_protocols,
		'security models': security_models,
		'ideal': ideal,
		'private sector classifications': private_sector_classifications,
	}
	return switcher.get(a, 'none')

def quiz(a):
	print(rtn())
	for item in a:
		question = "Name one of the %s items " % (len(a))
		prompt_user = raw_input(question)
		if prompt_user in a:
			print("correct")
			corrects.append(prompt_user)
			print(rtn())
		else:
			print("incorrect")
			incorrects.append(prompt_user)
			print(rtn())
		a = set(a) - set(corrects)

def print_list():
	for item in lst:
		print(item)

# import csvs
# build lists
osi = [
	'application',
	'presentation',
	'session',
	'transport',
	'network',
	'data link',
	'physical',  
]

firewalls = [
	'static packet filtering',
	'application-level gateway',
	'circuit-level gateway',
	'stateful inspection',
]

bcp = [
	'scope and planning',
	'business impact assessment',
	'continuity planning',
	'adoption and implementation',
]

biometrics = [
	'face scans',
	'fingerprints',
	'hand geometry',
	'heart/pulse patterns',
	'iris scans',
	'keystroke patterns',
	'palm scans',
	'retina scans',
	'signature dynamics',
	'voice pattern recognition',
	]

data_link_layer_protocols = [
	'SLIP',
	'PPP',
	'ARP',
	'RARP',
	'L2F',
	'L2TP',
	'PPTP',
	'ISDN',
]

session_layer_protocols = [
	'NFS',
	'SQL',
	'RPC',
]

security_models = [
	'security_models',
	'trusted computer base',
	'state machine',
	'information flow',
	'noninterference',
	'take-grant',
	'bell-lapadula',
	'biba',
	'clark-wilson',
	'brewer and nash (aka chinese wall)',
	'goguen-meseguer',
	'sutherland',
	'graham-denning',
]

ideal = [
	'initiating',
	'diagnosing',
	'establishing',
	'acting',
	'learning',
]

private_sector_classifications = [
	'public',
	'sensitive',
	'private',
	'confidential',
]

corrects = []
incorrects = []
lst = []

# prompt user
# validate user input
topic = raw_input("What would you like to drill?\na. osi layers\nb. firewalls\nc. business continuity planning\nd. biometrics\ne. data link layer protocols\nf. session layer protocols\ng. security models\nh. ideal model\ni. private sector classifications ")

# run function
value = choice_switch(topic)
a = value_switch(value)

# loop through list, ask user to name all of them items in lst
# if user answers correctly, add that answer to the corrects list and remove same from lst
# if user answers incorrectly, add that answer to the incorrects list and remove same from lst
quiz(a)

# for readability
print(rtn())

lst = set(a) - set(corrects)

if len(incorrects) == 0:
	print("100%. Great job!")
elif len(incorrects) == 1:
	print("Item for Review".upper())
	print_list()
else:
	print("Items for Review".upper())
	print_list()

print(rtn())