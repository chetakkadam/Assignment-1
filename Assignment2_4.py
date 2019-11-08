import math

def DivSum(n):
	result = 0;
	for i in range(2,(int)(math.sqrt(n))+1):
		if (n % i == 0):
			if (i == n / i):
				result += i;
			else:
				result += (i + n / i);
	return result + n + 1;

def main():
	number = input("Please Enter Number to calculate factor addition : ");
	value = DivSum(int(number));
	print("Addition of facto number of :", number, "is = ", value);
	
if __name__ == "__main__":
	main();