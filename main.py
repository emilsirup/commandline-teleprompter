import importlib
import time
import argparse
import sys
import os
from os import system
import keyboard

from titleDecoder import *

parser = argparse.ArgumentParser(description='Run a teleprompter from your terminal')
parser.add_argument('-f', '--file', metavar="", required=True, help='Paste the directory and name of the file you want the teleprompter to output')
parser.add_argument('-s','--seconds', type=int, metavar="", required=True, help='Input the amount of seconds you want the telepromter to use to print your text')
parser.add_argument('-tc','--titlecard', metavar="", required=False, help='Input the titlecard you want to be shown before you start (optional)\nNOTE: If your title has spaces, please add quotes around them.')
args = parser.parse_args()

f = open(args.file).read()

def bigchungus(title):
    arthonize(title)
    f = open("Title/Result.txt").read()
    print(f)

def titleSetup():
    if args.titlecard != "":
        bigchungus(args.titlecard)
        system("title " + args.titlecard)
    else:
        system("title " + "Commandline Teleprompter")

def start():
    for c in f + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(args.seconds / len(f))

os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal

titleSetup()

while True:
    try:
        if keyboard.is_pressed('space'):
            start()
    except:
        break
