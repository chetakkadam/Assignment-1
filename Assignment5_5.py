def recursive_factorial(num):
	if num == 1:  
		return num  
	else:  
		return num*recursive_factorial(num-1)

def main():
	n = int(input("Enter a Number : "));
	if n > 0:
		number = recursive_factorial(n);
	print("The factorial of ", n, " is ", number);
if __name__ == "__main__":
	main();