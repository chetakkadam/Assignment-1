def printpattern(number):
	if number < 1:
		return;
	print("*", end = " ");
	printpattern(number - 1);

def main():
	n = 5;
	printpattern(n);
if __name__ == "__main__":
	main();