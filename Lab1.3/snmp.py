from pysnmp.hlapi import *


class Snmp_exception(Exception): pass


def print_snmp(g):
    """Takes a generator object from pysnmp, prints snmp values"""
    # Actual request performs here.
    for snmp_result in g:
        errorIndication, errorStatus, errorIndex, varBinds = snmp_result
        if errorIndication:
            print(errorIndication)
            raise Snmp_exception
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            raise Snmp_exception
        else:
            for varBind in varBinds:
                print(varBind)
                print(' = '.join([x.prettyPrint() for x in varBind]))

try:
    g = getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.209', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

 
    print_snmp(g)

  
    n = nextCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.209', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
               lexicographicMode=False)

    print_snmp(n)
except:
   
    print('Error - exception')