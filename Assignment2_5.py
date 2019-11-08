import math

def checkprime(n):
	if n > 1 :
		for i in range(2, n//2):
			if(n % i == 0):
				print(n, " is not prime number");
				break;
		else:
			print(n, " is a Prime Number");
	else:
		print(n, " is a Prime Number");
			

def main():
	number = input("Pl provide number to check if prime : ");
	result = checkprime(int(number));
	
if __name__ == "__main__":
	main();
	