#!/usr/bin/python3
import time
from googlesearch import search
web=input("Enter topic to search:")
url=[]
for i in search(web,stop=10):
	print(i)
	time.sleep(1)
	url.append(i)
print(url)
