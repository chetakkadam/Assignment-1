from MarvellousNum import *;

def main():
	number = int(input("Number of Elements : "));
	primelist = list();
	lst = list();
	for i in range(0,number):
		element = int(input("Input Elements : "));
		lst.append(element);
		result = checkprime(int(element));
		print(result);
		if	result == True:
			primelist.append(element);
	primeAddition(primelist);
		
def primeAddition(numlist):
	totprimr = 0;
	if len(numlist) > 0:
		print(len(numlist));
		for	i in range(0, len(numlist)):
			totprimr = numlist[i] + totprimr;
	print("Output : ", totprimr);
			
if __name__ == "__main__":
	main();