import math

def printstar(n):
	for i in range(0,n):
		for j in range(n,i,-1):
			print("*", end=" ");
		print("\r");

def main():
	val = input("Pl enter a number : ");
	printstar(int(val));

if __name__ == "__main__":
	main();