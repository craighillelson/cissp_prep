from lists import *

rtn = lambda : '\n'

def choice_switch(a):
	choices
	return choices.get(a, "none")

def value_switch(a):
	choices = {
		'osi layers': osi,
		'application layer protocols': application_layer_protocols,
		'presentation layer protocols': presentation_layer_protocols,
		'transport layer protocols': transport_layer_protocols,
		'network layer protocols': network_layer_protocols,
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