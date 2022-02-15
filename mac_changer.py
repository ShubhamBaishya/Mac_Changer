#!usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="New MAC Address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an Interface ,use --help for more info")
    
    elif not options.new_mac:
        parser.error("[-] Please Specify a new MAC ,use --help for more info")
    return options




def change_mac(interface,new_mac):
    print("[+] Changing mac address for"+" "+ interface + " "+"to"+" " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
 
options=get_arguments()
change_mac(options.interface,options.new_mac)

