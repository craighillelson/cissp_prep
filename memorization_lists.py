# build dictionary
choices = {
	'a': 'osi layers',
	'b': 'firewalls',
	'c': 'bcp',
	'd': 'biometrics',
	'e': 'data link layer protocols',
	'f': 'session layer protocols',
	'g': 'security models',
	'h': 'ideal',
	'i': 'private sector classifications',
	'j': 'access controls',
	'k': 'aaa services',
	'l': 'defense in depth',
	'm': 'cryptographic attacks',
}

# define lambda and functions
rtn = lambda : '\n'

def choice_switch(a):
	choices
	return choices.get(a, 'none')

def value_switch(a):
	choices = {
		'osi layers': osi,
		'firewalls': firewalls,
		'bcp': bcp,
		'biometrics': biometrics,
		'data link layer protocols': data_link_layer_protocols,
		'session layer protocols': session_layer_protocols,
		'security models': security_models,
		'ideal': ideal,
		'private sector classifications': private_sector_classifications,
		'access controls': access_controls,
		'aaa services': aaa_services,
		'defense in depth': defense_in_depth,
		'cryptographic attacks': cryptographic_attacks,
	}
	return choices.get(a, "none")

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
from lists import *

# prompt user
# validate user input
print(rtn())
print("choices".upper())
for k, v in choices.items():
	print("%s %s") % (k, v)

print(rtn())

question = "What would you like to drill? "
topic = raw_input(question)

# run functions
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

# write results to a file

print(rtn())