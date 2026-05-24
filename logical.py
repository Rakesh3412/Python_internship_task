a=input("enter the  first statement \n")
b=input("enter the second statement \n")
st_1=eval(a)
st_2=eval(b)
operator=input("select the operator 'and','or','not'\n ")
if operator=='and':
	print(st_1 and st_2)
elif operator=='or':
	print(st_1 or st_2)
elif operator=='not':
	statement=int(input("select the statement 1 or 2 \n"))
	if statement==1:
		print(not st_1)
	else:
		print(not st_2)
else:
	print("invalid operator")