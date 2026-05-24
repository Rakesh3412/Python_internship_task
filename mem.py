statement_1=input("enter the statement \n")
word=input("enter the entire word or character to find in the statement \n")
op=input("select the operators 'in','not in' \n")
if op=='in':
	print(word in statement_1)
elif op=='not in':
	print(word not in statement_1)
else:
	print("Invlaid operator")
	
	