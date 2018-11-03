# for readability
rtn = lambda: '\n'

# header
print("formulas".upper())

# build dictionary
formulas = {
	'exposure factor': '%',
	'sle': 'av * ef',
	'aro': '# / year',
	'ale': 'sle * aro or av * ef * aro',
	'acs': '$ / year',
	'value of acs': '(ale1 - ale2) - acs',
}

# create list to be populated later
incorrects = []

# readability
print(rtn())

# quiz user
for k, v in formulas.items():
	user_answer = raw_input(k+" ")
	if user_answer == v:
		print("correct")
	else:
		see_answer = raw_input("Incorrect. Would you like to see the correct answer? ")
		incorrects.append(k)
		if see_answer == 'yes':
			print(v)
		else:
			pass
	print(rtn())

# show user what needs review
print("items for review".upper())
for item in incorrects:
	print(item)