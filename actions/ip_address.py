import re

from netifaces import interfaces, ifaddresses, AF_INET


WORDS = {
    'ip_address': {
        'groups': [
            'ip', ['ip', 'address'], ['network', 'address']
        ]
    }
}


def ip_address(text):
    ips = ""
    for ifaceName in interfaces():
        addresses = [
            i['addr'] for i in
            ifaddresses(ifaceName).setdefault(
                AF_INET, [{'addr': None}])]
        if None in addresses:
            addresses.remove(None)
        if addresses and ifaceName != "lo":
            updated_addresses = [re.sub(r"\.", r".", address)
                                 for address in addresses]
            list(updated_addresses)
            ips = str("I.P. Address: " + str(updated_addresses[0]))
            break
    return ips
