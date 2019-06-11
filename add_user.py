#!usr/bin/python3
import os
import crypt
usrname=raw_input()
count=0
for i in usrname:
        if i.isdigit():
                count=1
if count == 0 :
        usrpass="hello"+usrname
        uenc = crypt.crypt(usrpass,"22")
        os.system("useradd -m -p" +uenc +" "+usrname)
