# import json

# define lambda and function
rtn = lambda : '\n'

def choice(a):
	switcher = {
		'a': 'osi layers',
		'b': 'firewalls',
		'c': 'bcp',
		'd': 'biometrics',
		'e': 'session_layer_protocols',
	}
	return switcher.get(a)

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

session_layer_protocols = [
	'NFS',
	'SQL',
	'RPC',
]

corrects = []
incorrects = []
lst = []

# prompt user
# validate user input
topic = raw_input("What would you like to drill?\na. osi layers\nb. firewalls\nc. business continuity planning\nd. biometrics\ne. session layer protocols ")

# run function
value = choice(topic)

# print(value)

if value == 'osi layers':
	a = osi
elif value == 'firewalls':
	a = firewalls
elif value == 'bcp':
	a = bcp
elif value = 'biometrics':
	a = biometrics
else:
	a = session_layer_protocols 
	

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