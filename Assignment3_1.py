def inputaddition(numlist):
	tot = 0;
	for i  in range(0, len(numlist)):
		tot = tot+numlist[i];
	print("Addition of Numbers : ", tot);


def main():
	lst = list();
	n = int(input("Enter Number of Element in List : "));
	for i in range(0, n):
		element = int(input());
		lst.append(element);
	inputaddition(lst);
	
if __name__ == "__main__":
	main();