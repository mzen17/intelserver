# Functions for server. 
# This is an internal module for all neccesary server functions.
# Splitting this allows for accuracy access

import dns.resolver
import socket
import ssl
import subprocess

def getIPv4(domain_name: str) -> str:
    # A is IPv4
    answers = dns.resolver.resolve(domain_name, 'A')

    # Concat all the answers together, since resolve returns an array.
    answer = str(answers[0])
    for i in range(1, len(answers)):
        answer += ("," + str(answers[i]))
    return (answer)


def getIPv6(domain_name: str) -> []:
    # AAAA is IPv6
    answers = dns.resolver.resolve(domain_name, 'AAAA')

    # Concat all the answers together, since resolve returns an array.
    answer = str(answers[0])
    for i in range(1, len(answers)):
        answer += ("," + str(answers[i]))
    return (answer)


def getSSL(domain_name: str) -> str:
    context = ssl.create_default_context()
    # SSL runs over 443, so connect to 443
    with context.wrap_socket(socket.socket(), server_hostname=domain_name) as ssock:
        ssock.connect((domain_name, 443))
        cert = ssock.getpeercert()
    return cert


def get_org(domain_name: str) -> str:
    cert = getSSL(domain_name)
    for i in cert['issuer']:
        if i[0][0] == 'organizationName':
            return str(i[0][1])
        
import os 
def get_asn(domain_name: str) -> str:
    try:
        ip = getIPv4(domain_name)
    except Exception:
        ip = ""

    if ( ip == ""):
        ip = getIPv6(domain_name)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    command = f"echo '{ip}' | nc whois.cymru.com 43"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    return output

