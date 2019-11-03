def calc_factorial(value1):
	factorial = 1;
	for i in range(1, value1 + 1):
		factorial = factorial * i;
	print("The factorial of ", value1,"is : ", factorial);
		
		
def factorial_call():
	value = int(input("Please enter a number :  "));
	calc_factorial(value);
	
factorial_call();