import os
import sys
from shutil import which
cmnd=input("Enter Command")
while(cmnd) :
	f=open("Commandlist",'a+')
	f.write(cmnd)
	for i in f :
		if(cmnd == i) :
			print("REPEATED")
			cmnd=input() 
		if(which(cmnd)) :
			os.system(cmnd)
		elif(cmnd == "exit") :
			sys.exit(0)		
		else :
			print("Command not found..")
			cmnd=input()
