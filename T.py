import os
import sys
import os.path
import random
from time import sleep as timeout
from core.starkmcore import *
from multiprocessing import Process
from termcolor import colored

print(colored("""
 ####################
    TAssistent
 ####################
 Insta @aniketstark330
 GitHub aniketstark
 ####################
 """, "green"))
checkfile()
def command():
 stark = raw_input("stark > ")
 if stark== "help":
  help()
 elif stark == "start phishing" or stark == "phishing":
  os.system("termux-tts-speak -r 0.9 ok. boss starting phishing")
  Phishing()
 elif stark == "start port forwarding" or stark  ==  "port forward":
  portforward()
 elif stark == "create payload" or stark == "payload":
  payload()
 elif stark == "startwebhacking" or stark == "webhacking":
  webhack()
 elif stark == "dork" or stark == "sqldork":
  sqldork()
 elif stark == "hash" or stark == "hasher" or stark == "hash decrypt":
  Hash()
 elif stark == "battery" or stark == "battery info":
  battery()
 elif stark == "capture photo" or stark == "photo":
  cphoto()
 elif stark == "text to speach" or stark == "textspeach":
  textspeach()
 elif stark == "clear":
  os.system("clear")
 elif stark == "hi" or stark == "hello" or stark == "whats up":
  print random.choice(hi)
 elif stark == "i am fine" or stark == "fine":
  print(colored("""Me Tooo ;)\n""", "green"))
 elif stark == "are you boy or girl" or stark == "are you boy" or stark == "are you girl":
  printslow(colored("""My Gender not decided XD\n""" , "yellow"))
 elif stark == "where are you from" or stark == "where you from":
  printslow(colored("""i am from python2 Termux XD\n""", "green"))
 elif stark == "who is your developer" or stark == "who is your boss" or stark == "who make you":
  printslow(colored("""My Developer is you because of you\n support my developer to make me thanks for that\n""", "green"))
  visit()
 elif stark == "credit" or stark == "credits":
  credit()
 elif stark == "thanks" or stark == "thank you":
  printslow(colored("""Glad You Like It XD\n""", "blue"))
 elif stark == "exit":
  exit()
 else:
      print  (colored("ERROR: Sorry sir my maker not added for this command", 'red'))
      timeout(2)
      command()
loop = True
while loop:
  command()

