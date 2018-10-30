choices = {
	'a': 'osi layers',
	'b': 'application layer protocols',
	'c': 'presentation layer protocols',
	'd': 'session layer protocols',
	'e': 'transport layer protocols',
	'f': 'network layer protocols',
	'g': 'data link layer protocols',
	'h': 'physical layer protocols',
	'i': 'firewalls',
	'j': 'bcp',
	'k': 'biometrics',
	'l': 'data link layer protocols',
	'm': 'session layer protocols',
	'n': 'security models',
	'o': 'ideal',
	'p': 'private sector classifications',
	'q': 'access controls',
	'r': 'aaa services',
	's': 'defense in depth',
	't': 'cryptographic attacks',
}

osi = [
	'application',
	'presentation',
	'session',
	'transport',
	'network',
	'data link',
	'physical',  
]

application_layer_protocols = [
	'HTTP',
	'FTP',
	'LPD',
	'SMTP',
	'Telnet',
	'TFTP',
	'EDI',
	'POP3',
	'IMAP',
	'SNMP',
	'NNTP',
	'S-RPC',
	'SET',
]

presentation_layer_protocols = [
	'ASCII',
	'EBCDICM',
	'TIFF',
	'JPEG',
	'MPEG',
	'MIDI',
]

transport_layer_protocols = [
	'TCP',
	'UDP',
	'SPX',
	'SSL',
	'TLS',
]

network_layer_protocols = [
	'ICMP',
	'RIP',
	'OSPF',
	'BGP',
	'IGMP',
	'IP',
	'IPSec',
	'IPX',
	'NAT',
	'SKIP',
]

data_link_layer_protocols = [
	'SLIP',
	'PPP',
	'ARP',
	'RARP',
	'L2F',
	'L2TP',
	'PPTP',
	'ISDN',
]

physical_layer_protocols = [
	'EIA/TIA-232 and EIA/TIA-449',
	'X.21',
	'HSSI',
	'SONET',
	'V.24 and V.35',
]

firewalls = [
	'static packet filtering',
	'application-level gateway',
	'circuit-level gateway',
	'stateful inspection',
]

bcp = [
	'scope and planning',
	'business impact assessment',
	'continuity planning',
	'adoption and implementation',
]

biometrics = [
	'face scans',
	'fingerprints',
	'hand geometry',
	'heart/pulse patterns',
	'iris scans',
	'keystroke patterns',
	'palm scans',
	'retina scans',
	'signature dynamics',
	'voice pattern recognition',
]

session_layer_protocols = [
	'NFS',
	'SQL',
	'RPC',
]

security_models = [
	'security_models',
	'trusted computer base',
	'state machine',
	'information flow',
	'noninterference',
	'take-grant',
	'bell-lapadula',
	'biba',
	'clark-wilson',
	'brewer and nash (aka chinese wall)',
	'goguen-meseguer',
	'sutherland',
	'graham-denning',
]

ideal = [
	'initiating',
	'diagnosing',
	'establishing',
	'acting',
	'learning',
]

private_sector_classifications = [
	'public',
	'sensitive',
	'private',
	'confidential',
]

access_controls = [
	'role-based access control',
	'rule-based access control',
	'mandatory access control',
	'discretionary access control',
]

aaa_services = [
	'authentication',
	'authorization',
	'accountability',
]

defense_in_depth = [
	'physical controls',
	'logical/technical controls',
	'administrative controls',
]

cryptographic_attacks = [
	'analytic attack',
	'implementation attack',
	'statistical attack',
	'brute force',
	'frequency analysis and the ciphertext only attack',
	'knows plaintext',
	'chosen ciphertext',
	'chosen plaintext',
	'meet in the middle',
	'man in the middle',
	'birthday',
	'replay',
]

corrects = []
incorrects = []
lst = []