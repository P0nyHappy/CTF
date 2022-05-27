#!/usr/bin/env python3
import string 

alfaber=string.ascii_lowercase+string.digits+'_'
print(alfaber)
print(len(alfaber))
print("string.ascii_lowercase->",len(string.ascii_lowercase))
print("string.digits->",len(string.digits))
file_read="message.txt"
flag=''

with open(file_read) as f:
	list_element=f.read().split()

	for element in list_element:
		print(element,"->",pow(int(element),-1,41))
		index_in_alfabet=pow(int(element),-1,41)
		flag+= alfaber[index_in_alfabet-1]
		#print(flag)
print("picoCTF{",flag,"}" , sep='')