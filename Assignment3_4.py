def FindNumFreq(numList, numtoFind):
	freq = {};
	count = 0;
	if len(numList) < 0:
		print("List has no Elements");
	else:
		for j in range(0, len(numList)):
			if(numList[j] == numtoFind):
				count = count + 1;
		print("Output : ", count);
		
		
		
def main():
	lst = list();
	n = int(input("Enter Number of Element : "));
	for i in range(0,n):
		element = int(input("Input Elements : "));
		lst.append(element);
	specNumber = int(input("Element to Search : "));
	FindNumFreq(lst, specNumber);
	
if __name__ == "__main__":
	main();