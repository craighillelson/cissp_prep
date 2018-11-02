# imports
import dicts
from lists import *

rtn = lambda : '\n'

def choice_switch(a):
	dicts.categories
	return dicts.categories.get(a, "none")

def value_switch(a):
	categories = {
		'osi layers': osi,
		'application layer protocols': application_layer_protocols,
		'presentation layer protocols': presentation_layer_protocols,
		'session layer protocols': session_layer_protocols,
		'transport layer protocols': transport_layer_protocols,
		'network layer protocols': network_layer_protocols,
		'data link layer protocols': data_link_layer_protocols,
		'physical layer protocols': physical_layer_protocols,
		'firewalls': firewalls,
		'bcp': bcp,
		'biometrics': biometrics,
		'security models': security_models,
		'ideal': ideal,
		'sw-cmm': swcmm,
		'private sector classifications': private_sector_classifications,
		'access controls': access_controls,
		'aaa services': aaa_services,
		'defense in depth': defense_in_depth,
		'cryptographic attacks': cryptographic_attacks,
		'incident response steps': incident_response_steps,
		'tcsec classes': tcsec_classes,
	}
	return categories.get(a, "none")

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