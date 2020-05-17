#!/usr/bin/python
#BomMail

import os
import smtplib
import getpass
import sys
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time
from colorama import init, Style, Back, Fore
def banner():
    print("""

    /$$$$$$$                          /$$      /$$           /$$ /$$      
    | $$__  $$                        | $$$    /$$$          |__/| $$      
    | $$  \ $$  /$$$$$$  /$$$$$$/$$$$ | $$$$  /$$$$  /$$$$$$  /$$| $$      
    | $$$$$$$  /$$__  $$| $$_  $$_  $$| $$ $$/$$ $$ |____  $$| $$| $$      
    | $$__  $$| $$  \ $$| $$ \ $$ \ $$| $$  $$$| $$  /$$$$$$$| $$| $$      
    | $$  \ $$| $$  | $$| $$ | $$ | $$| $$\  $ | $$ /$$__  $$| $$| $$      
    | $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$ \/  | $$|  $$$$$$$| $$| $$$$$$$$
    |_______/  \______/ |__/ |__/ |__/|__/     |__/ \_______/|__/|________/
                                                                                    
    """)
def BomEmail():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def send(to):
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        if smtp_server == "smtp.gmail.com":
                server.starttls()
        server.login(user,passwd)
        for i in range(1, total+1):
            msg = 'From: ' + user + '\nSubject: ' + str(subject) + '\n' + body
            server.sendmail(user,to,msg)
            print ("\r[+]E-mails sent: %i" % i)
            sys.stdout.flush()
        server.quit()
        print('\n Done  !!!')
        print( '                                                  BomMail :~ Enjoy :)')
    except KeyboardInterrupt:
        print( '[-] Canceled')
        sys.exit()
    except smtplib.SMTPAuthenticationError:
        print ('\n[!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps')
        sys.exit()


if __name__ == '__main__':
    # l = []
    # with open('list.txt','r') as mail:
    #     to = mail.readlines()
    # for x in to:
    #     l.append(x)
    BomEmail()
    banner()
    server = input ('MailServer 1.Gmail/2.Yahoo: ')
    user = 'unknown.dza@gmail.com'
    passwd = 'gmail19960811'
    #to = input('\nTo: ')
    to = []
    with open('list.txt',"r") as data:
        l=data.readlines()
    for x in l:
        to.append(x)

    subject = input('Subject: ')
    body = input('Message: ')
    total = int(input('Number of send for everyone: '))
    if server == 'gmail' or '1' or 'Gmail':
        smtp_server = 'smtp.gmail.com'
        port = 587
    elif server == 'yahoo' or '2' or 'Yahoo':
        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
    else:
        print('Kindly Enter Your Answer in 1 or 2 in Mail Server.')
        sys.exit()
    print('')
    pool = ThreadPool(10)
    pool.map(send, to)
    pool.close()
    pool.join()



    #---------------------
   
#user = input('Email: ')

#passwd = getpass.getpass('Password: ')


