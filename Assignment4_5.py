from functools import *;
def DataInputFromUser():
	user_list = list();
	n = int(input("Enter Number of Element: "));
	for i in range(0,n):
		print("Pl enter number: ", i+1);
		element = int(input());
		user_list.append(element);
	return user_list;
	
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
		boolresult = True;
		# print(n, " is a Prime Number");
	return boolresult;
			

def main():
	Userdata = DataInputFromUser();
	FilteredData = list();
	for i in range(0, len(Userdata)):
		checkres = checkprime(Userdata[i]);
		if(checkres == True):
			FilteredData.append(Userdata[i]);
	print(FilteredData);
	ModifiedData = list(map(lambda x: (x * 2), FilteredData));
	print(ModifiedData);
	FinalData = reduce(lambda x,y: max(x,y), ModifiedData);
	print("Max Number :", FinalData);	

if __name__ == "__main__":
	main();