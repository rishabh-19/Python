#pip install pyqrcode and google
import webbrowser
import pyqrcode
from pyqrcode import QRCode
from googlesearch import search
data=input("Enter data to be searched: ")
f=open('/var/www/html/qr.html','w')
urls = [i for i in search(data,stop=3)]
j=0
for i in range(len(urls)):
    url=pyqrcode.create(urls[i])
    q=open("/var/www/html/"+data+str(i)+".svg",'wb')
    url.svg(q,scale=8)
    f.write('<img src="'+data+str(i)+".svg"+'">')
    j+=1
ip=input("Enter ip to search: ")
webbrowser.open(ip+'/qr.html')
f.close()
q.close()
