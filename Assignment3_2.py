def main():
	lst = list();
	n = int(input("Number of Elements : "));
	for i in range(0,n):
		element = int(input("Pl Enter number "));
		lst.append(element);
	print("Output : ", max(lst));
		
if __name__ == "__main__":
	main();
		
	