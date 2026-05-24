a=int(input("enter the first number\n"))
b=int(input("enter the second number\n"))
operator=input("select the operator '+','-','*','/','%','//','**'\n")
if operator=='+':
	sum=a+b
	print("sum of two numbers=",sum)
elif operator=='-':
	sub=a-b
	print("subtraction of two numbers",sub)
elif operator=='*':
	pro=a*b
	print("Multiplication of two numbers=",pro)
elif operator=='/':
	div=a/b
	print("Division of two numbers=",div)
elif operator=='%':
	modulo=a%b
	print("modulo division of two numbers=",modulo)
elif operator=='//':
	floor_division=a//b
	print("floor division of two numbers=",floor_division)
elif operator=='**':
	exponential=a**b
	print("exponential of two numbers is=",exponential)
else:
	print("invalid operator \n")