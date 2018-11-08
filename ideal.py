# define lambda
rtn = lambda: '\n'

# define ideal list
ideal = [
	'initiating',
	'diagnosing',
	'establishing',
	'acting',
	'learning',
	]

i = 0

# quiz user
for item in ideal:
	prompt_user = raw_input("name one of the elements ")
	if prompt_user == ideal[i]:
		print("correct")
		print(rtn())
	else:
		print("Incorrect. The correct answer is %s") % (ideal[i])
		print(rtn())
	i = i + 1