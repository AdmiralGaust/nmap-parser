# nmap-parser
nmap-parser is a python script is to parse the nmap scan results in a quick time.It allows the users to search for a specific vulnerability in the scan result and the script will provide all the ips along with their ports having that particular vulnerabilty.
# Quick-Installation
git clone https://github.com/AdmiralGaust/nmap-parser.git
# Usage
1. cd into the folder nmap-parser

2. open the nmap-parser.py file with your favourite text editor

3. search for the line
keyword_list=["sweet32","rc4","cbc","rsa"]

4. Now, replace the keywords with the vulnerabilities which you want to search and save the changes

5. python nmap-parser.py <input filename>


