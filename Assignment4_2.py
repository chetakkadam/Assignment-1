def main():
	num1 = int(input("Please Enter Number 1 : "));
	num2 = int(input("Please Enter Number 2 : "));
	result = lambda x,y: x * y;
	print("Multiplication of Numbers ", num1," & ", num2, " : ", result(num1,num2));
	
if __name__ == "__main__":
	main();