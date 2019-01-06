""" __doc__ """

OSI = [
    'application',
    'presentation',
    'session',
    'transport',
    'network',
    'data link',
    'physical',
]

APPLICATION_LAYER_PROTOCOLS = [
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

PRESENTATION_LAYER_PROTOCOLS = [
    'ASCII',
    'EBCDICM',
    'TIFF',
    'JPEG',
    'MPEG',
    'MIDI',
]

TRANSPORT_LAYER_PROTOCOLS = [
    'TCP',
    'UDP',
    'SPX',
    'SSL',
    'TLS',
]

NETWORK_LAYER_PROTOCOLS = [
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

DATA_LINK_LAYER_PROTOCOLS = [
    'SLIP',
    'PPP',
    'ARP',
    'RARP',
    'L2F',
    'L2TP',
    'PPTP',
    'ISDN',
]

PHYSICAL_LAYER_PROTOCOLS = [
    'EIA/TIA-232 and EIA/TIA-449',
    'X.21',
    'HSSI',
    'SONET',
    'V.24 and V.35',
]

FIREWALLS = [
    'static packet filtering',
    'application-level gateway',
    'circuit-level gateway',
    'stateful inspection',
]

BCP = [
    'scope and planning',
    'business impact assessment',
    'continuity planning',
    'adoption and implementation',
]

BIOMETRICS = [
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

SESSION_LAYER_PROTOCOLS = [
    'NFS',
    'SQL',
    'RPC',
]

SECURITY_MODELS = [
    'trusted computing base',
    'state machine',
    'information flow',
    'noninterference',
    'take-grant',
    'access control matrix',
    'bell-lapadula',
    'biba',
    'clark-wilson',
    'brewer and nash (aka chinese wall)',
    'goguen-meseguer',
    'sutherland',
    'graham-denning',
]

IDEAL = [
    'initiating',
    'diagnosing',
    'establishing',
    'acting',
    'learning',
]

SWCMM = [
    'initiating',
    'repeatable',
    'defined',
    'managed',
    'optimized',
]

PRIVATE_SECTOR_CLASSIFICATIONS = [
    'public',
    'sensitive',
    'private',
    'confidential',
]

ACCESS_CONTROLS = [
    'role-based access control',
    'rule-based access control',
    'mandatory access control',
    'discretionary access control',
]

AAA_SERVICES = [
    'authentication',
    'authorization',
    'accountability',
]

DEFENSE_IN_DEPTH = [
    'physical controls',
    'logical/technical controls',
    'administrative controls',
]

CRYPTOGRAPHIC_ATTACKS = [
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

INCIDENT_RESPONSE_STEPS = [
    'detection',
    'response',
    'mitigation',
    'reporting',
    'recovery',
    'remediation',
    'lessons learned',
]

TCSEC_CLASSES = [
    'a - verified protection',
    'b - mandatory protection',
    'c - discretionary protection',
    'd - minimal protection',
]

VIRUS_PROPOGATION = [
    'mbr',
    'file infection',
    'macro',
    'service injection',
]

CORRECTS = []
INCORRECTS = []
LST = []
