bin_num_1=input("Enter the first binary  number= ")
bin_num_2=input("Enter the second binary number= ")
num_1=int(bin_num_1,2)
num_2=int(bin_num_2,2)
print("SIMPLE BITWISE CALCULATOR")
operator=input("select the operator '&','|','^','~','>>','<<' \n")
if operator=='&':
	bit_and=num_1 & num_2
	print("bit wise and operator on first and second number=",bin(bit_and))
	print("the natural number is=",bit_and)
elif operator=='|':
	bit_or=num_1 | num_2
	print("bit wise or operator on first and second number=",bin(bit_or))
	print("the natural number is =",bit_or)
elif operator=='^':
	bit_xor=num_1 ^ num_2
	print("bit wise xor operator on first and second number=",bin(bit_not))
	print("the natural number is =",bit_xor)
elif operator=='~':
	bit_not_1=~num_1
	bit_not_2=~num_2
	print("bit wise not operator on frist number= ",bin(bit_not_1))
	print("bit wise not operator on second number= ",bin(bit_not_2))
	print("the natural number is =",bit_not_1)
	print("the natural number is =",bit_not_2)
elif operator=='>>':
	number=int(input("enter number of bits to move"))
	bit_right_1=num_1 >> number
	bit_right_2=num_2 >> number
	print("bit wise right_shift operator on first number=",bin(bit_right_1))
	print("the natural number is =",bit_right_1)
	print("bit wise right_shift operator on  second number=",bin(bit_right_2))
	print("the natural number is =",bit_right_2)
elif operator=='<<':
	number=int(input("Enter number of bits to left shift "))
	bit_left_1=num_1 << number
	bit_left_1=num_2 << number
	print("bit wise left_shift operator on first and second number=",bin(bit_left_1))
	print("the natural number is =",bit_left_1)
	print("bit wise left_shift operator on  second number=",bin(bit_left_2))
	print("the natural number is =",bit_left_2)
else:
	print("invalid operator \n")
