def printpattern(number, smallnumber = 1):
	if number < 1:
		return;
	print(smallnumber, end = " ");
	if (smallnumber < number):
		printpattern(number, smallnumber + 1);

def main():
	n = 5;
	printpattern(n);
if __name__ == "__main__":
	main();