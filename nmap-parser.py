#!/usr/bin/python

import re
from sys import argv

try:
    file = open(argv[1])
    data = file.read()
except:
    print"Plese specify the input file as first argument"
    exit()

#Fill this list with  keywords you want to search for
keyword_list=["sweet32","rc4","cbc","rsa"]


#This Function return the data of all ports as a list, the len of list is being equal to the number of ports  
def find_port_data(data):
    all_ports_data = re.split('SERVICE',data)
    all_ports_data = all_ports_data[1]
    all_ports_data=all_ports_data.splitlines()
    all_ports_data.reverse()
    one_port_data = ''
    ports_data = []
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in all_ports_data:
        if i.startswith(tuple(num)):
            one_port_data +=i
            ports_data.append(one_port_data)
            one_port_data=''
        else:
            one_port_data+=i
    return ports_data


#Global variables
one_ip_result = re.split('Nmap scan report for',data)

print"\n\n"
print " "*6 + "-"*55
for data in one_ip_result:
    try:
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',data).group()
    except:
        continue

    ports_data = find_port_data(data)

    for port_data in ports_data:
        if re.search(r'\d{1,3}/',port_data):
            port = re.search(r'\d*/',port_data).group()
            port = port[:-1]
            for keyword in keyword_list:
                if re.search(keyword,port_data,re.I):
                    print " "*6 + "| %20s | %5s | %20s |" %(ip,port,keyword)
                    print" " *6 + "-"*55



