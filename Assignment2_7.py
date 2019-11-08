def printval(n):
	num = 1;
	for i in range(0,n):
		num = 1;
		for j in range(0,n):
			print(num, end=" ");
			num = num+1;
		print("\r");

def main():
	val = input("Pl enter a number : ");
	printval(int(val));

if __name__ == "__main__":
	main();