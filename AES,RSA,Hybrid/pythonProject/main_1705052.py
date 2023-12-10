from BitVector import *
import pprint as pp
import numpy as np
import copy
import time

from bitvectordemo import Sbox, InvSbox

from_main_text = [[],[],[],[]]

start_for_decryption = 0.0
start_for_encryption =0.0


# text_data= input('Enter your textdata: ')

# key_text= input('Enter your keydata: ')
round_array = [
        BitVector(hexstring="00"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="04"),
        BitVector(hexstring="08"), BitVector(hexstring="10"), BitVector(hexstring="20"), BitVector(hexstring="40"),
        BitVector(hexstring="80"), BitVector(hexstring="1B"), BitVector(hexstring="36")
    ]



def gfunction(list1,r_n):
    global round_array

    listtemp = list1[0]
    list1[0] = list1[1]
    list1[1] = list1[2]
    list1[2] = list1[3]
    list1[3] = listtemp

    for gg in range(4):
        HEXVALUE_G = list1[gg].get_bitvector_in_hex()
        b0 = BitVector(hexstring=HEXVALUE_G)
        int_val0 = b0.intValue()
        s0 = Sbox[int_val0]
        s0 = BitVector(intVal=s0, size=8)
        list1[gg] = s0
        gg =gg+1

    list1[0] = list1[0] ^ round_array[r_n]
    # print("after rounding :")
    # print(list1[0].get_bitvector_in_hex())

    return


def round_key_generation(round_number,list_key,round_key_array):
    # round_number = 1
    list_origin = [[],[],[],[]]
    list_origin[0] = list_key[0].copy()
    list_origin[1] = list_key[1].copy()
    list_origin[2] = list_key[2].copy()
    list_origin[3] = list_key[3].copy()


    # print('key')
    #
    # for iik in range(4):
    #     for jjk in range(4):
    #         print(list_origin[iik][jjk].get_bitvector_in_hex())
    #     iik = iik + 1
    # jjk = jjk + 1

    gfunction(list_key[3],round_number)

    for rki in range(4):
        list_key[0][rki] = list_key[0][rki] ^ list_key[3][rki]
        rki = rki+1

    for rki1 in range(4):
        list_key[1][rki1] = list_key[0][rki1] ^ list_key[1][rki1]
        rki1 = rki1+1

    for rki2 in range(4):
        list_key[2][rki2] = list_key[1][rki2] ^ list_key[2][rki2]
        rki2 = rki2+1

    for rki3 in range(4):
        list_key[3][rki3] = list_key[2][rki3] ^ list_origin[3][rki3]
        rki3 = rki3+1

    # print('after xor')
    # for i_g in range(4):
    #     for j_g in range(4):
    #         print(list_key[i_g][j_g].get_bitvector_in_hex())
    #     i_g = i_g + 1
    # j_g = j_g + 1

    return

def Mixed_Columns(string,round_key_k,list_text,round_key_array):

    # global list_text

    list_onop = [[],[],[],[]]
    if(string=='Encryption'):
        mixed = [[],[],[],[]]
        t1 = BitVector(hexstring="02")
        t2 = BitVector(hexstring="03")
        t3 = BitVector(hexstring="01")
        t4 = BitVector(hexstring="01")
        hex_1 = t1.get_bitvector_in_hex()
        hex_2 = t2.get_bitvector_in_hex()
        hex_3 = t3.get_bitvector_in_hex()
        hex_4 = t4.get_bitvector_in_hex()
        mixed[0].append(BitVector(hexstring=hex_1))
        mixed[0].append(BitVector(hexstring=hex_2))
        mixed[0].append(BitVector(hexstring=hex_3))
        mixed[0].append(BitVector(hexstring=hex_4))

        t5 = BitVector(hexstring="01")
        t6 = BitVector(hexstring="02")
        t7 = BitVector(hexstring="03")
        t8 = BitVector(hexstring="01")
        hex_5 = t5.get_bitvector_in_hex()
        hex_6 = t6.get_bitvector_in_hex()
        hex_7 = t7.get_bitvector_in_hex()
        hex_8 = t8.get_bitvector_in_hex()
        mixed[1].append(BitVector(hexstring=hex_5))
        mixed[1].append(BitVector(hexstring=hex_6))
        mixed[1].append(BitVector(hexstring=hex_7))
        mixed[1].append(BitVector(hexstring=hex_8))

        t9 = BitVector(hexstring="01")
        t10 = BitVector(hexstring="01")
        t11 = BitVector(hexstring="02")
        t12 = BitVector(hexstring="03")
        hex_9 = t9.get_bitvector_in_hex()
        hex_10 = t10.get_bitvector_in_hex()
        hex_11 = t11.get_bitvector_in_hex()
        hex_12 = t12.get_bitvector_in_hex()
        mixed[2].append(BitVector(hexstring=hex_9))
        mixed[2].append(BitVector(hexstring=hex_10))
        mixed[2].append(BitVector(hexstring=hex_11))
        mixed[2].append(BitVector(hexstring=hex_12))

        t13 = BitVector(hexstring="03")
        t14 = BitVector(hexstring="01")
        t15 = BitVector(hexstring="01")
        t16 = BitVector(hexstring="02")
        hex_13 = t13.get_bitvector_in_hex()
        hex_14 = t14.get_bitvector_in_hex()
        hex_15 = t15.get_bitvector_in_hex()
        hex_16 = t16.get_bitvector_in_hex()
        mixed[3].append(BitVector(hexstring=hex_13))
        mixed[3].append(BitVector(hexstring=hex_14))
        mixed[3].append(BitVector(hexstring=hex_15))
        mixed[3].append(BitVector(hexstring=hex_16))


        for ii in range(4):
            for jj in range(4):
                data0 = [0, 0, 0, 0]
                for kk in range(4):
                    hex_text = list_text[kk][jj].get_bitvector_in_hex()
                    hex_mixed = mixed[ii][kk].get_bitvector_in_hex()
                    AES_modulus = BitVector(bitstring='100011011')
                    bv1 = BitVector(hexstring=hex_mixed)
                    bv2 = BitVector(hexstring=hex_text)
                    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                    data0[kk] = bv3

                list_onop[ii].append(data0[0] ^ data0[1] ^ data0[2] ^ data0[3])


        list_text = list_onop.copy()
        # print('mixed columns',round_key_k)
        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(),list_text[i_g][1].get_bitvector_in_hex(),list_text[i_g][2].get_bitvector_in_hex(),list_text[i_g][3].get_bitvector_in_hex())
        #     i_g = i_g + 1

        string5 = 'Encryption'
        Add_round_Key(string5,round_key_k,list_text,round_key_array)

    elif(string=='Decryption'):
        mixed = [[], [], [], []]
        t1 = BitVector(hexstring="0E")
        t2 = BitVector(hexstring="0B")
        t3 = BitVector(hexstring="0D")
        t4 = BitVector(hexstring="09")
        hex_1 = t1.get_bitvector_in_hex()
        hex_2 = t2.get_bitvector_in_hex()
        hex_3 = t3.get_bitvector_in_hex()
        hex_4 = t4.get_bitvector_in_hex()
        mixed[0].append(BitVector(hexstring=hex_1))
        mixed[0].append(BitVector(hexstring=hex_2))
        mixed[0].append(BitVector(hexstring=hex_3))
        mixed[0].append(BitVector(hexstring=hex_4))

        t5 = BitVector(hexstring="09")
        t6 = BitVector(hexstring="0E")
        t7 = BitVector(hexstring="0B")
        t8 = BitVector(hexstring="0D")
        hex_5 = t5.get_bitvector_in_hex()
        hex_6 = t6.get_bitvector_in_hex()
        hex_7 = t7.get_bitvector_in_hex()
        hex_8 = t8.get_bitvector_in_hex()
        mixed[1].append(BitVector(hexstring=hex_5))
        mixed[1].append(BitVector(hexstring=hex_6))
        mixed[1].append(BitVector(hexstring=hex_7))
        mixed[1].append(BitVector(hexstring=hex_8))

        t9 = BitVector(hexstring="0D")
        t10 = BitVector(hexstring="09")
        t11 = BitVector(hexstring="0E")
        t12 = BitVector(hexstring="0B")
        hex_9 = t9.get_bitvector_in_hex()
        hex_10 = t10.get_bitvector_in_hex()
        hex_11 = t11.get_bitvector_in_hex()
        hex_12 = t12.get_bitvector_in_hex()
        mixed[2].append(BitVector(hexstring=hex_9))
        mixed[2].append(BitVector(hexstring=hex_10))
        mixed[2].append(BitVector(hexstring=hex_11))
        mixed[2].append(BitVector(hexstring=hex_12))

        t13 = BitVector(hexstring="0B")
        t14 = BitVector(hexstring="0D")
        t15 = BitVector(hexstring="09")
        t16 = BitVector(hexstring="0E")
        hex_13 = t13.get_bitvector_in_hex()
        hex_14 = t14.get_bitvector_in_hex()
        hex_15 = t15.get_bitvector_in_hex()
        hex_16 = t16.get_bitvector_in_hex()
        mixed[3].append(BitVector(hexstring=hex_13))
        mixed[3].append(BitVector(hexstring=hex_14))
        mixed[3].append(BitVector(hexstring=hex_15))
        mixed[3].append(BitVector(hexstring=hex_16))

        for ii in range(4):
            for jj in range(4):
                data0 = [0, 0, 0, 0]
                for kk in range(4):
                    hex_text = list_text[kk][jj].get_bitvector_in_hex()
                    hex_mixed = mixed[ii][kk].get_bitvector_in_hex()
                    AES_modulus = BitVector(bitstring='100011011')
                    bv1 = BitVector(hexstring=hex_mixed)
                    bv2 = BitVector(hexstring=hex_text)
                    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
                    data0[kk] = bv3

                list_onop[ii].append(data0[0] ^ data0[1] ^ data0[2] ^ data0[3])

        list_text = list_onop.copy()
        # print('mixed columns', round_key_k)
        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(), list_text[i_g][1].get_bitvector_in_hex(),
        #           list_text[i_g][2].get_bitvector_in_hex(), list_text[i_g][3].get_bitvector_in_hex())
        #     i_g = i_g + 1

        string5 = 'Decryption'
        Shift_Rows(string5, round_key_k, list_text,round_key_array)


    else:
        print('no see')


    return



def Shift_Rows(string,round_key_k,list_text,round_key_array):
    # global round_array
    # global list_text

    if (string == 'Encryption'):
        temp_4 = list_text[1][0]
        temp_5 = list_text[1][1]
        temp_6 = list_text[1][2]
        temp_7 = list_text[1][3]
        temp_8 = list_text[2][0]
        temp_9 = list_text[2][1]
        temp_10 = list_text[2][2]
        temp_11 = list_text[2][3]
        temp_12 = list_text[3][0]
        temp_13 = list_text[3][1]
        temp_14 = list_text[3][2]
        temp_15 = list_text[3][3]

        list_text[1][0] = temp_5
        list_text[1][1] = temp_6
        list_text[1][2] = temp_7
        list_text[1][3] = temp_4
        list_text[2][0] = temp_10
        list_text[2][1] = temp_11
        list_text[2][2] = temp_8
        list_text[2][3] = temp_9
        list_text[3][0] = temp_15
        list_text[3][1] = temp_12
        list_text[3][2] = temp_13
        list_text[3][3] = temp_14

        # print('after shift rows',round_key_k)
        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(),list_text[i_g][1].get_bitvector_in_hex(),list_text[i_g][2].get_bitvector_in_hex(),list_text[i_g][3].get_bitvector_in_hex())
        #     i_g = i_g + 1

        string4 = 'Encryption'
        if(round_key_k>=10):
            Add_round_Key(string4,round_key_k,list_text,round_key_array)
        else:
            Mixed_Columns(string4,round_key_k,list_text,round_key_array)


    elif (string == 'Decryption'):
        temp_4 = list_text[1][0]
        temp_5 = list_text[1][1]
        temp_6 = list_text[1][2]
        temp_7 = list_text[1][3]
        temp_8 = list_text[2][0]
        temp_9 = list_text[2][1]
        temp_10 = list_text[2][2]
        temp_11 = list_text[2][3]
        temp_12 = list_text[3][0]
        temp_13 = list_text[3][1]
        temp_14 = list_text[3][2]
        temp_15 = list_text[3][3]

        list_text[1][0] = temp_7
        list_text[1][1] = temp_4
        list_text[1][2] = temp_5
        list_text[1][3] = temp_6
        list_text[2][0] = temp_10
        list_text[2][1] = temp_11
        list_text[2][2] = temp_8
        list_text[2][3] = temp_9
        list_text[3][0] = temp_13
        list_text[3][1] = temp_14
        list_text[3][2] = temp_15
        list_text[3][3] = temp_12

        # print('after shift rows', round_key_k)
        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(), list_text[i_g][1].get_bitvector_in_hex(),
        #           list_text[i_g][2].get_bitvector_in_hex(), list_text[i_g][3].get_bitvector_in_hex())
        #     i_g = i_g + 1

        string4 = 'Decryption'
        # conditions will change
        Substitution_byte(string4, round_key_k,list_text,round_key_array)

    else:
        print('no see')

    return


def Substitution_byte(string,round_key_k,list_text,round_key_array):
    # global list_text

    if(string=='Encryption'):
        for gg in range(4):
            for hh in range(4):
                HEXVALUE_G = list_text[gg][hh].get_bitvector_in_hex()
                b0 = BitVector(hexstring=HEXVALUE_G)
                int_val0 = b0.intValue()
                s0 = Sbox[int_val0]
                s0 = BitVector(intVal=s0, size=8)
                list_text[gg][hh] = s0
                hh = hh + 1
            gg = gg + 1

        # print('after substitution byte',round_key_k)
        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(),list_text[i_g][1].get_bitvector_in_hex(),list_text[i_g][2].get_bitvector_in_hex(),list_text[i_g][3].get_bitvector_in_hex())
        #     i_g = i_g + 1

        String3 = 'Encryption'
        Shift_Rows(String3,round_key_k,list_text,round_key_array)

    elif(string=='Decryption'):
        for gg in range(4):
            for hh in range(4):
                HEXVALUE_G = list_text[gg][hh].get_bitvector_in_hex()
                b0 = BitVector(hexstring=HEXVALUE_G)
                int_val0 = b0.intValue()
                s0 = InvSbox[int_val0]
                s0 = BitVector(intVal=s0, size=8)
                list_text[gg][hh] = s0
                hh = hh + 1
            gg = gg + 1

        # print('after substitution byte',round_key_k)
        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(),list_text[i_g][1].get_bitvector_in_hex(),list_text[i_g][2].get_bitvector_in_hex(),list_text[i_g][3].get_bitvector_in_hex())
        #     i_g = i_g + 1

        String3 = 'Decryption'
        Add_round_Key(String3,round_key_k,list_text,round_key_array)

    else:
        print('no see')


    return


def Add_round_Key(string,round_key_k,list_text,round_key_array):
    global from_main_text

    if(string=='Encryption'):

        for ii in range(4):
            for jj in range(4):
                list_text[ii][jj] = list_text[ii][jj] ^ round_key_array[round_key_k][ii][jj]

        # print('after add round',round_key_k)

        string1='Encryption'
        round_key_ = round_key_k + 1

        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(),list_text[i_g][1].get_bitvector_in_hex(),list_text[i_g][2].get_bitvector_in_hex(),list_text[i_g][3].get_bitvector_in_hex())

        if (round_key_ >= 11):
            # print('after add round', round_key_k)
            trans_temp = [[], [], [], []]
            trans = [[], [], [], []]

            for iirk in range(4):
                for jjrk in range(4):
                    hexvalue_kkl = list_text[iirk][jjrk].get_bitvector_in_hex()
                    trans_temp[iirk].append(hexvalue_kkl)

            trans = np.transpose(trans_temp)

            for iir in range(4):
                for jjr in range(4):
                    h = trans[iir][jjr]
                    list_text[iir][jjr] = h

            # final = []
            # for ii1 in range(4):
            #     for jj1 in range(4):
            #         val = list_text[ii1][jj1].intValue()
            #         final.append(val)
            #
            # jp = ''.join([chr(i) for i in final])

            # cipherText = jp
            global from_main_text
            from_main_text = copy.deepcopy(list_text)
            # print('list_text',list_text)
            # print('from main ',from_main_text)
            end_for_encryption = time.time()
            time_en = end_for_encryption - start_for_encryption
            print('the encryption time for aes',time_en)
            return from_main_text
        else:
            Substitution_byte(string1,round_key_,list_text,round_key_array)

    elif(string=='Decryption'):
        for ii in range(4):
            for jj in range(4):
                list_text[ii][jj] = list_text[ii][jj] ^ round_key_array[round_key_k][ii][jj]

        # print('after add round',round_key_k)

        string1='Decryption'
        round_key_ = round_key_k - 1

        # for i_g in range(4):
        #     print(list_text[i_g][0].get_bitvector_in_hex(),list_text[i_g][1].get_bitvector_in_hex(),list_text[i_g][2].get_bitvector_in_hex(),list_text[i_g][3].get_bitvector_in_hex())

        if(round_key_k == 10 ):
            Shift_Rows(string1, round_key_, list_text,round_key_array)
        elif(round_key_k == 0):
            trans_temp = [[], [], [], []]
            trans = [[], [], [], []]

            for iirk in range(4):
                for jjrk in range(4):
                    hexvalue_kkl = list_text[iirk][jjrk].get_bitvector_in_hex()
                    trans_temp[iirk].append(hexvalue_kkl)

            trans = np.transpose(trans_temp)

            for iir in range(4):
                for jjr in range(4):
                    h = trans[iir][jjr]
                    list_text[iir][jjr] = BitVector(hexstring=h)

            final = []
            for ii1 in range(4):
                for jj1 in range(4):
                    val = list_text[ii1][jj1].intValue()
                    final.append(val)

            jp = ''.join([chr(i) for i in final])
            from_main_text[0].append(jp)

            end_for_decryption = time.time()
            time_end = end_for_decryption - start_for_decryption
            print('the decryption time for aes', time_end)
            return from_main_text
        elif(round_key_k < 10):
            Mixed_Columns(string1,round_key_,list_text,round_key_array)



    else:
        print('no see')


    return


def every_round_key(string_,list_text,list_key,round_key_array):

    if (string_ == 'Encryption'):
        start = time.time()
        # print('type',type(start))
        for rounds in range(1,11):
            round_key_generation(rounds,list_key,round_key_array)
        # round_key_array[rounds] = list_key.copy()
            for iirk in range(4):
                for jjrk in range(4):
                    hexvalue_kkl = list_key[iirk][jjrk].get_bitvector_in_hex()
                    round_key_array[rounds][iirk].append(BitVector(hexstring=hexvalue_kkl))

        for r_r in range(1,11):
            trans_temp21 = [[], [], [], []]
            trans21 = [[], [], [], []]

            for iirk21 in range(4):
                for jjrk21 in range(4):
                    hexvalue_kkl21 = round_key_array[r_r][iirk21][jjrk21].get_bitvector_in_hex()
                    trans_temp21[iirk21].append(hexvalue_kkl21)
        # print(trans_temp)
            trans21 = np.transpose(trans_temp21)
        # print(trans)
            for iir21 in range(4):
                for jjr21 in range(4):
                    h21 = trans21[iir21][jjr21]
                # print("print",iir,jjr,h)
                    round_key_array[r_r][iir21][jjr21] = BitVector(hexstring=h21)

            # for roundsk in range(11):
            #     print('every round key func', roundsk)
            #     for iik in range(4):
            #         print(round_key_array[roundsk][iik][0].get_bitvector_in_hex(),round_key_array[roundsk][iik][1].get_bitvector_in_hex(),round_key_array[roundsk][iik][2].get_bitvector_in_hex(),
            #         round_key_array[roundsk][iik][3].get_bitvector_in_hex())
        end_t = time.time()

        t_time = end_t - start
        print('key scheduling in Encryption : ',t_time)

        string='Encryption'
        round_key_ = 0
        Add_round_Key(string,round_key_,list_text,round_key_array)

    elif(string_ == 'Decryption'):
        start_t1 =time.time()
        for rounds in range(1,11):
            round_key_generation(rounds, list_key, round_key_array)
        # round_key_array[rounds] = list_key.copy()
            for iirk in range(4):
                for jjrk in range(4):
                    hexvalue_kkl = list_key[iirk][jjrk].get_bitvector_in_hex()
                    round_key_array[rounds][iirk].append(BitVector(hexstring=hexvalue_kkl))

        for r_r in range(1,11):
            trans_temp21 = [[], [], [], []]
            trans21 = [[], [], [], []]

            for iirk21 in range(4):
                for jjrk21 in range(4):
                    hexvalue_kkl21 = round_key_array[r_r][iirk21][jjrk21].get_bitvector_in_hex()
                    trans_temp21[iirk21].append(hexvalue_kkl21)
        # print(trans_temp)
            trans21 = np.transpose(trans_temp21)
        # print(trans)
            for iir21 in range(4):
                for jjr21 in range(4):
                    h21 = trans21[iir21][jjr21]
                # print("print",iir,jjr,h)
                    round_key_array[r_r][iir21][jjr21] = BitVector(hexstring=h21)

        # for roundsk in range(11):
        #     print('every round key func', roundsk)
        #     for iik in range(4):
        #         print(round_key_array[roundsk][iik][0].get_bitvector_in_hex(),round_key_array[roundsk][iik][1].get_bitvector_in_hex(),round_key_array[roundsk][iik][2].get_bitvector_in_hex(),
        #             round_key_array[roundsk][iik][3].get_bitvector_in_hex())

        end_t1 = time.time()

        t1_time = end_t1 - start_t1
        print('key scheduling in Decryption : ', t1_time)
        string='Decryption'
        round_key_ = 10
        Add_round_Key(string,round_key_,list_text,round_key_array)



        return

def Operations(string,text_data,list_key,round_key_array):
    if(string=='Encryption'):

        start_for_encryption = time.time()
        # print(text_data)
        s_text = text_data.encode('utf-8')
        hex_convert_text = s_text.hex()
        binVal_text = BitVector(hexstring=hex_convert_text)
        # print(hex_convert_text)
        list_text = [[], [], [], [], []]
        for i in range(4):
            for j in range(4):
                hexvalue = binVal_text.get_bitvector_in_hex()[((i * 8) + j * 2):((i * 8) + j * 2 + 2)]
                list_text[i].append(BitVector(hexstring=hexvalue))

        trans_temp = [[], [], [], []]
        trans = [[], [], [], []]

        for iirk in range(4):
            for jjrk in range(4):
                hexvalue_kkl = list_text[iirk][jjrk].get_bitvector_in_hex()
                trans_temp[iirk].append(hexvalue_kkl)

        trans = np.transpose(trans_temp)

        for iir in range(4):
            for jjr in range(4):
                h = trans[iir][jjr]
                list_text[iir][jjr] = BitVector(hexstring=h)

        every_round_key(string,list_text,list_key,round_key_array)


    elif(string=='Decryption'):
        start_for_decryption = time.time()
        # s_text = input('Enter the ciphertext:')
        # # hex_convert_text = s_text.hex()
        # # binVal_text = BitVector(hexstring=hex_convert_text)
        # # print(hex_convert_text)
        list_text = [[], [], [], [], []]
        for i in range(4):
            for j in range(4):
                hexvalue = text_data[i][j]
                # h = hexvalue.hex()
                list_text[i].append(BitVector(hexstring=hexvalue))

        trans_temp = [[], [], [], []]
        trans = [[], [], [], []]

        for iirk in range(4):
            for jjrk in range(4):
                hexvalue_kkl = list_text[iirk][jjrk].get_bitvector_in_hex()
                trans_temp[iirk].append(hexvalue_kkl)

        trans = np.transpose(trans_temp)

        for iir in range(4):
            for jjr in range(4):
                h = trans[iir][jjr]
                list_text[iir][jjr] = BitVector(hexstring=h)

        every_round_key(string, list_text,list_key,round_key_array)

    return

def Calling(string_1,text_data,key_text):

    s_key = key_text.encode('utf-8')
    hex_convert_key = s_key.hex()

    binVal_key = BitVector(hexstring=hex_convert_key)
    # print(hex_convert_key)
    # print(binVal_key)

    # round_key_array = [[],[],[],[],[],[],[],[],[],[],[]]
    round_key_array = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []],
                          [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []],
                          [[], [], [], []]]

    # print(len(round_key_array[0]))

    list_key = [[], [], [], [], []]
    for ik in range(4):
        for jk in range(4):
            hexvalue_k = binVal_key.get_bitvector_in_hex()[((ik * 8) + jk * 2):((ik * 8) + jk * 2 + 2)]
            list_key[ik].append(BitVector(hexstring=hexvalue_k))
        jk = jk + 2
    ik = ik + 1

    # print('Before assigning')
    # for iil in range(4):
    #     print(list_text[iil][0].get_bitvector_in_hex(),list_text[iil][1].get_bitvector_in_hex(),
    #         list_text[iil][2].get_bitvector_in_hex(),
    #         list_text[iil][3].get_bitvector_in_hex())

    # round_key_array[0]= list_key.copy()

    for ii_ in range(4):
        for jj_ in range(4):
            hexvalue_kk = list_key[ii_][jj_].get_bitvector_in_hex()
            round_key_array[0][ii_].append(BitVector(hexstring=hexvalue_kk))
            jj_ = jj_ + 2
        ii_ = ii_ + 1

    trans_temp1 = [[], [], [], []]
    trans1 = [[], [], [], []]

    for iirk1 in range(4):
        for jjrk1 in range(4):
            hexvalue_kkl1 = round_key_array[0][iirk1][jjrk1].get_bitvector_in_hex()
            trans_temp1[iirk1].append(hexvalue_kkl1)

    trans1 = np.transpose(trans_temp1)
    for iir1 in range(4):
        for jjr1 in range(4):
            h1 = trans1[iir1][jjr1]
            round_key_array[0][iir1][jjr1] = BitVector(hexstring=h1)

    Operations(string_1,text_data,list_key,round_key_array)
    return from_main_text


# string_1 = 'Decryption'
# key_text = 'Thats my Kung Fu'
# text_data = 'Two One Nine Two'
# Calling(string_1,text_data,key_text)



