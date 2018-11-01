# define functions
def correct():
	print("correct")

def incorrect():
	print("incorrect")

# populate dictionary
network_cabling_types = {
	'10Base2': [
		'10 Mbps',
		'185 meters',
		'medium',
		'medium',
		'medium',
	],
	'10Base5': [
		'10 Mbps',
		'500 meters',
		'high',
		'low',
		'high',
	],
	'10Base-T (UTP)': [
		'10 Mbps',
		'100 meters',
		'low',
		'high',
		'Very low',
	],
	'STP': [
		'155 Mbps',
		'100 Mbps',
		'medium',
		'medium',
		'high',
	],
	'100Base-T/100BaseTX': [
		'100 Mbps',
		'100 meters',
		'low',
		'high',
		'low',
	],
	'1000Base-T': [
		'1 Gbps',
		'100 meters',
		'low',
		'high',
		'medium',
	],
	'Fiber-optic': [
		'2+ Gbps',
		'2+ kilometers',
		'very high',
		'none',
		'very high',
	],
}

# quiz user
for k, v in sorted(network_cabling_types.iteritems()):
	# prompt_user = raw_input(k)
	print(k)
	max_speed = raw_input("Max speed: ")
	if max_speed == v[0]:
		correct()
	else:
		incorrect()
	distance = raw_input("Distance: ")
	if distance == v[1]:
		correct()
	else:
		incorrect()
	difficulty = raw_input("Difficulty: ")
	if difficulty == v[2]:
		correct()
	else:
		incorrect()
	susceptibility = raw_input("Susceptibility: ")
	if susceptibility == v[3]:
		correct()
	else:
		incorrect()
	cost = raw_input("Cost: ")
	if cost == v[4]:
		correct()
	else:
		incorrect()
	print('\n')