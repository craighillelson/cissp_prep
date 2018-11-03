# imports
import csv
import random

# define lambda and function
rtn = lambda : '\n'

def choice_switcher(a):
	switcher = {
		'a': '802.11',
		'b': 'attacks',
		'c': 'formulas',
		'd': 'laws',
		'e': 'osi',
		'f': 'protocols_ports',
	}
	return switcher.get(a, 'none')

# create lists to be populated later
terms = []
definitions = []
corrects = []
incorrects = []

user_choice = raw_input("What would you like to drill\na. 802.11\nb. attacks\nc. formulas\nd. laws\ne. osi\nf. protocols and ports ")
user_choice = choice_switcher(user_choice)
user_choice_csv = user_choice+'.csv'
print(rtn())

# import a csv with terms and definitions and populate lists of terms and definitions
with open(user_choice_csv) as f:
	f_csv = csv.DictReader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	for row in f_csv:
		terms.append(row['term'])
		definitions.append(row['definition'])

# print("There are %s terms in this list.") % len(terms)
number_to_drill = int(raw_input("There are %s terms in this list. How many terms would you like to drill? " % len(terms)))
random_numbers = random.sample(range(0, len(terms)), number_to_drill)

# for readability
print(rtn())

# loop through terms, quiz user, and add correct and incorrect answers to respective lists
for i in random_numbers:
	print(rtn())
	prompt = "Term: %s\nDefinition: " % (terms[i])
	user_answer = raw_input(prompt) 
	if user_answer == definitions[i]:
		print("Correct!")
		corrects.append(terms[i])
	else:
		print("Incorrect")
		print("%s") % (definitions[i])
		incorrects.append(terms[i])

# update user on their performance
# get length of each set of answers
num_correct = len(corrects)
num_inconnect = len(incorrects)

print(rtn())

percentage_correct = float(len(corrects)) / float(len(random_numbers))
print("You defined %s of the terms you attempted correctly.") % ("{0:.0%}".format(percentage_correct))

print(rtn())

print("%s %s") % ("Correct Answers:", num_correct)
for correct in corrects:
	print(correct)

print(rtn())

if len(incorrects) > 0:
	print("%s %s") % ("Incorrect Answers:", num_inconnect)
	print("Review the following:")
	for incorrect in incorrects:
		print(incorrect)

print(rtn())