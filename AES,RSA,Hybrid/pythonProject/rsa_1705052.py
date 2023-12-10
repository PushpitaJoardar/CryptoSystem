import random
import time
import numpy as np

# text_data = 'Two One Nine Two'
# key_text = 'Thats my Kung Fu'

def rabinMiller(num: int) -> bool:
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def GenerationOfTwoPrimes(key_):
    prime = 0
    com1 = pow(2, (key_ - 1)) + 1
    com1 = int(com1)
    com2 = pow(2, (key_))
    com2 = int(com2)
    for i in range(com1,com2, 2):
        if rabinMiller(i):
            if prime != 0:
                return prime, i

            prime = i
    return


def GenerationOfedn(k):

    p, q = GenerationOfTwoPrimes(int(k//2))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 1
    for i in range(1, phi_n + 1):
        if phi_n % i == 0 and phi_n % i == 0:
            e = i
            break

    d = pow(e, -1, phi_n)

    return e, d, n


def Encryption(e_, n_, string):

    e_ = int(e_)
    n_ = int(n_)

    ascii_values = []
    for character in string:
        ascii_values.append(ord(character))
    # print(ascii_values)

    counter = 0
    for ii in ascii_values:
        counter = counter + 1

    ciphertext = []
    for c_ in range(counter):
        temp = pow(ascii_values[c_], e_, n_)
        ciphertext.append(temp)

    # print('Ciphertext: ')

    return ciphertext

def Decryption(d_, n_, ascii_values):

    counter = 0
    for ii in ascii_values:
        counter = counter + 1

    ciphertext = []
    for c_ in range(counter):
        temp = pow(ascii_values[c_], d_, n_)
        ciphertext.append(temp)
    # print(ciphertext)

    return ''.join([chr(i) for i in ciphertext])


# key_ = input('enter key : ', )
def begin_func(key_,operation,string):
    # key_ = int(key_)
    start = time.time()
    e, d, n = GenerationOfedn(key_)
    if(operation=='Encryption'):
        cipher = Encryption(e, n, string)
        end_t = time.time()
        time_t = end_t - start
        print('time of encryption & key : ',time_t,key_)
        return cipher

    elif(operation=='Decryption'):
        real = Decryption(d, n, string)
        end_tn = time.time()
        time_tn = end_tn - start
        print('time of decryption & key : ', time_tn, key_)
        return real

# text = begin_func(128,'Encryption','Two One Nine Two')
# print(text)





