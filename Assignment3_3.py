def main():
	lst = list();
	n = int(input("Enter Number of Elements : "));
	for i in range(0,n):
		element = int(input("Enter a Number : "));
		lst.append(element);
	print("Output : ", min(lst));
	
if __name__ == "__main__":
	main();