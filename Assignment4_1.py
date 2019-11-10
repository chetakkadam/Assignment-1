def main():
	num = int(input("Please Enter Number : "));
	result = lambda x: 2 ** x;
	print("Power of Number : ", num, "is ", result(num));

if __name__ == "__main__":
	main();