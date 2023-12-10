import socket
import pickle
from rsa_1705052 import *
from main_1705052 import *

s = socket.socket()
key_ =128
port = 12345
s.connect(('127.0.0.1', port))
data_key = [[],[],[],[]]
data_text = [[],[],[],[]]

file1 = open("Don’t Open this", "r")
print("Output of Read function is ")
full_line = file1.read()
x = full_line.split(",")
print('private key:')
d = x[0]
n = x[1]
print('d',d)
print('n',n)

e_ = s.recv(1024)
e = pickle.loads(e_)
# print(e)
# e = print(s.recv(1024).decode())
s.send('Got from server'.encode())
# n= print(s.recv(1024).decode())
n_ = s.recv(1024)
n = pickle.loads(n_)
print('public key',e,n)
s.send('Got it from server'.encode())

data_key = s.recv(1024)
myvar = pickle.loads(data_key)
print('the encrypted key: ',myvar)
s.send('Got the encrypted key'.encode())

data_text = s.recv(1024)
myvar1 = pickle.loads(data_text)
print('the encrypted text: ',myvar1)
s.send('Got the ciphertext'.encode())

plain_key=begin_func(key_,'Decryption',myvar)
print('key after decryption :',plain_key)

from_ = Calling('Decryption',myvar1,plain_key)
print('in bob end, the plain text :',from_[0][0])

real_text = input("Enter the real text for matching :",)
if(real_text== from_[0][0]):
    s.send('The encryption and Decryption was successful!Now the End.'.encode())
    print('The encryption and Decryption was successful!Now the End.')







s.close()
