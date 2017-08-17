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

one_ip_result = re.split('Nmap scan report for',data)
keyword_port_dict = {}
keyword_port = {}
result = {}

for data in one_ip_result:
    port_data = re.split('SERVICE',data)
    try:
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',data).group()
    except:
        continue
    for p in port_data:
        try:
            port = re.search(r'\d*/',p).group()
            port = port[:-1]
        except:
            continue
        for keyword in keyword_list:
            if re.search(keyword,p,re.I):
                keyword_port[keyword]=port
        keyword_port_dict[port] = keyword_port
    result[ip] = keyword_port_dict


print" "*4  + "_"*64
for i in result:
    for j in result[i]:
        for k in result[i][j]:
            print " "*4 + "| " + i +" "*(19-len(i))+ "| " + j + " "*(19-len(j)) + "| " + k + " "*(19-len(k)) + "|"
    print " "*4 + "|" + "_"*62 + "|"


