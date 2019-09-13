import os
import csv

port = raw_input("Enter port to scan (eg: 1-65535):")

f = open ("host.txt", "r")
f1 = f.readlines()

f = open ("result.csv", "w+")

for address in f1:
 address = address.rstrip()
 os.system('nmap -p %s %s | awk \'{print $2}\' > tmp' % (port, address))
 g = open ("tmp", "r")
 lines = g.readlines()
 #print lines[5]
 f.write("%s,%s" % (address, lines[5]))
