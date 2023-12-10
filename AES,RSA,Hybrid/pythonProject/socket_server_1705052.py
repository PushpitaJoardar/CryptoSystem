
import socket
import time
import pickle

from rsa_1705052 import *
from main_1705052 import *

RSA_key = input('RSA key: ',)
RSA_key = int(RSA_key)
AES_key = input('AES key : ',)
Plaintext = input('Enter Plaintext : ',)
from_ = Calling('Encryption',Plaintext,AES_key)
print('In server the encryted plain text :',from_)
list = begin_func(RSA_key,'Encryption',AES_key)
print('the encrypted RSA key:',list)

e, d, n = GenerationOfedn(RSA_key)

with open("Don’t Open this","w") as fileinput:
    fileinput.write(str(d))
    fileinput.write(',')
    fileinput.write(str(n))

s = socket.socket()
print ("Socket successfully created")

port = 12345
s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")

while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    data_key = [[],[],[],[]]
    data_text = [[],[],[],[]]

    e_ = pickle.dumps(e)
    c.send(e_)
    print(c.recv(1024).decode())
    n_ = pickle.dumps(n)
    c.send(n_)
    print(c.recv(1024).decode())
    data_key = pickle.dumps(list)
    c.send(data_key)
    data_text = pickle.dumps(from_)
    c.send(data_text)
    print(c.recv(1024).decode())

    print(c.recv(1024).decode())

    print(c.recv(1024).decode())


c.close()

