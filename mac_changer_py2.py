#!/bin/python2.7

import subprocess
import optparse

'''
subprocess is a module, OptionParser() is a class of that module. parser is an instance of OptionParser()
which can handle parsing for us
'''


def get_parse_arguments():
    parser = optparse.OptionParser()

    # Giving a parser the arguments it can expect from users (-i and --interface to specify the interface).
    # dest="interface" mean is the name where the value of the interface is going to be stored and help is a
    # help message.
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use -h or --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for: " + interface + " to: " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


if __name__ == '__main__':
    options = get_parse_arguments()
    change_mac(options.interface, options.new_mac)


'# interface --> wlp2s0'