def printnumdigits(n):
	number = n;
	count = 0;
	while(n>0):
		count=count+1;
		n=n//10;
	print("Number of Digits in ", number, " : ", count);
	
def main():
	val = input("Pl enter a Number: ");
	printnumdigits(int(val));
	
if __name__ == "__main__":
	main();