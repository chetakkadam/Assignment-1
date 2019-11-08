def additionofdigits(n):
	number = n;
	total = 0;
	while(n>0):
		dig=n%10;
		total=total+dig;
		n=n//10;
	print("Addition of digits of ",number, " : ", total);

def main():
	val = input("Pl enter a Number : ");
	additionofdigits(int(val));
	
if __name__ == "__main__":
	main();