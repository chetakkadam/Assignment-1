import math

def checkprime(n):
	boolresult = False;
	if n > 1 :
		for i in range(2, n//2):
			if(n % i == 0):
				# print(n, " is not prime number");
				boolresult = False;
				break;
		else:
			boolresult = True;
			# print(n, " is a Prime Number");
	else:
		return boolresult;
		# print(n, " is a Prime Number");
	