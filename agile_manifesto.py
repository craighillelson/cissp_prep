# define lambda for readability
rtn = lambda : '\n'

# populate dictionary
agile_manifesto_dict = {
	'people and interactions': 'processes and tools',
	'working software': 'comprehensive documentation',
	'customer collaboration': 'contract negotiation',
	'responding to change': 'following a plan',
}

# announce topic
print(rtn())
print("agile manifesto".upper())

# loop through dictionary and prompt user for the b sections in the response to a sections
for k, v in agile_manifesto_dict.items():
	print("%s") % (k)
	prompt_user = raw_input("over\n")
	if prompt_user == v:
		print("correct")
	else:
		print("incorrect")
	print(rtn())
