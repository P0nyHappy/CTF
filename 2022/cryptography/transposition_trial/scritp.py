
with open("message.txt") as text:
	my_read_text_in_file=text.read()

flag=''
for i in range(0,len(my_read_text_in_file),3):
	check=my_read_text_in_file[i:i+3]
	a,b,c=check
	flag+=c+a+b
print(flag)