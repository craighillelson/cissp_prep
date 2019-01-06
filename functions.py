""" __doc__ """

# imports
import dicts
from lists import *

RTN = lambda: "\n"

def choice_switch(a):
    """ switch statement based on user choice """
    dicts.categories
    return dicts.categories.get(a, "none")

def value_switch(a):
    """ switch statement to associate user choice with topic variable """
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
        'swcmm': swcmm,
        'private sector classifications': private_sector_classifications,
        'access controls': access_controls,
        'aaa services': aaa_services,
        'defense in depth': defense_in_depth,
        'cryptographic attacks': cryptographic_attacks,
        'incident response steps': incident_response_steps,
        'tcsec classes': tcsec_classes,
        'virus propogation': virus_propogation,
    }
    return categories.get(a, "none")

def quiz(a):
    """ quiz """
    print RTN()
    hint = raw_input("""Before taking the quiz,
                     would you like to review the items in this category? """)
    if hint == 'yes':
        print RTN()
        for item in a:
            print item
    else:
        pass
    print RTN()
    for item in a:
        question = "Name one of the %s items " % (len(a))
        prompt_user = raw_input(question)
        if prompt_user in a:
            print "correct"
            corrects.append(prompt_user)
            print RTN()
        else:
            print "incorrect"
            incorrects.append(prompt_user)
            print RTN()
        a = set(a) - set(corrects)

def print_list():
    """ loop through list, print results """
    for item in lst:
        print item
