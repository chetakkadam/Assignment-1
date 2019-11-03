def Add(value1, value2):
	return print("Addition : ", value1 + value2);
	
def Sub(value1, value2):
	return print("Subtraction : ", value1 - value2);
	
def Mult(value1, value2):
	return print("Multiplication : ", value1 * value2);
	
def Div(value1, value2):
	return print("Division : ", value1 / value2);

def Marvellous():
	value1 = int(input("Please enter first number : "));
	value2 = int(input("Please enter second number : "));
	value3 = input("Please enter operation : add/sub/mult/div :  ");
	if value3 == "add":
		Add(value1, value2);
	elif value3 == "sub":
		Sub(value1, value2);
	elif value3 == "mult":
		Mult(value1, value2);
	elif value3 == "div":
		Div(value1, value2);
		
Marvellous();