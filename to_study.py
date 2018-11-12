# for readability
rtn = lambda: '\n'

# define function
def choice_to_file(a):
    switcher = {
        'a': 'formulas.py',
        'b': 'protocols_ports.py',
        'c': 'ports_protocols.py',
        'd': 'symmetric_memorization_chart.py',
        'e': 'hash_algorithm_memorization_chart.py',
        'f': 'network_cabling_types.py',
        'g': 'name_that_layer.py',
        'h': 'ideal.py',
        'i': 'swcmm.py',
        'j': 'water_suppression_systems.py',
    }
    return switcher.get(a, 'nothing')

# offer the user some choices of lists to drill
user_choice = raw_input(
    "What would you like to study?\n"
    "a. formulas\n"
    "b. protocols and ports\n"
    "c. ports and protocols\n"
    "d. symmetric memorization chart\n"
    "e. hash algorithm memorization chart\n"
    "f. network cabling types\n"
    "g. which layer?\n"
    "h. ideal\n"
    "i. swcmm\n"
    "j. water suppression systems\n"
    )

# run function an load the file of the user's choice
file = choice_to_file(user_choice)
print(rtn())
execfile(file)