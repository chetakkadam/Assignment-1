def UserEnteredData():
	userlist = list();
	n = int(input("Enter Number of Elements : "));
	for i in range(0, n):
		print("Pl enter number ", i);
		elements = int(input());
		userlist.append(elements);
	return userlist;
	
def summation(lst):
	if len(lst) == 0:
		return 0;
	else:
		return lst[0] + summation(lst[1:]);

def main():
	data = UserEnteredData();
	print(data);
	addition =  summation(data);	
	print("Addition : ", addition);
	
if __name__ == "__main__":
	main();