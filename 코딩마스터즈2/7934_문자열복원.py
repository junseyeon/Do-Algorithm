# -*- coding: utf-8 -*-
import sys

def decode(encoded_str):
    decoded_str = ""
    i = 0

    while i < len(encoded_str):
        if i + 2 < len(encoded_str) and encoded_str[i + 2] == '0':  # a가 10 이상일 때
            if i+3 < len(encoded_str) and encoded_str[i+3] =='0':
                decoded_str += chr(int(encoded_str[i]) + 96)
                decoded_str += chr(int(encoded_str[i+1:i + 3]) + 96)
                i+=4
            else:
                decoded_str += chr(int(encoded_str[i:i + 2]) +96)
                #print(encoded_str[i:i + 2])
                i += 3
        else:
            # a가 9 이하일 때
            decoded_str += chr(int(encoded_str[i]) +96)
            i += 1

    return decoded_str

encoded_result = input()
decoded_result = decode(encoded_result)
print(decoded_result)

