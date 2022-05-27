#!/usr/bin/evn python3 
import string

alfabet = string.ascii_uppercase+ string.digits+'_'
file_name= "message.txt"

def read_3_elements():


	f = open(file_name, "r")
	for i in range(21):
	
		first_3_number =int(f.read(4))
		#print(first_3_number,end="->")
		#print(first_3_number % 37,end='\n')
		print(alfabet[(first_3_number % 37)-1],end='')

def optinizate_open_file():
	string=''
	with open(file_name) as temp:
		st = temp.read().split()
	print(st)
	for i in st:
		print(i,"->",int(i)%37)
		string+=alfabet[(int(i)%37)]
	print(string)
#read_3_elements()


optinizate_open_file()