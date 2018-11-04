rtn = lambda: '\n'

def print_correct():
	print("Correct")

def print_incorrect():
	print("Incorrect. The correct answer is: ")

symmetric_memorization_chart = {
	'Advanced Encyption Standard (AES)': [
		'128', 
		'128, 192, 256',
	],
	'Rijndael': [
		'Variable', 
		'128, 192, 256',
	],
	'Blowfish (often used in SSH)': [
		'64', 
		'32-448',
	],
	'Data Encyption Standard (DES)': [
		'64', 
		'56',
	],
	'IDEA (used in PGP)': [
		'64', 
		'128',
	],
	'Rivest Cipher 2 (RC2)': [
		'64', 
		'128',
	],
	'Rivest Cipher 4 (RC4)': [
		'Streaming', 
		'128',
	],
	'Rivest Cipher 5 (RC5)': [
		'32, 64, 128',
		'0-2,040',
	],
	'Skipjack': [
		'64', 
		'80',
	],
	'Triple DES (3DES)': [
		'64',
		'112 or 168',
	],
	'Twofish': [
		'128', 
		'1-256',
	],
}

# corrects = []
incorrects = []

print(rtn())

for k, v in symmetric_memorization_chart.items():
	print(k)
	name = k
	block_size = v[0]
	key_size = v[1]
	user_answer = raw_input("block size: ")
	if user_answer == v[0]:
		print_correct()
	else:
		print_incorrect()
		print(v[0])
		incorrects.append(name)
	user_answer = raw_input("key size: ")
	if user_answer == v[1]:
		print_correct()
	else:
		print_incorrect()
		print(v[1])
		incorrects.append(name)
	print(rtn())

print("items for review".upper())
for name in incorrects:
	print(name)