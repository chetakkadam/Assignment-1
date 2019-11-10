from functools import *;

def AcceptData():
	arr = list();
	n = int(input("Enter Number of Elements : "));
	print("Pl enter elements:");
	for i in range(0,n):
		print("Pl enter number ", i+1);
		element = int(input());
		arr.append(element);
	return arr;
	
def main():
	rawlist = AcceptData();
	print(rawlist);
	FilterList = list(filter(lambda x:((x>=70)&(x<=90)),rawlist));
	print(FilterList);
	ModifiedList = list(map(lambda x:(x+10), FilterList));
	print(ModifiedList);
	ProductList = reduce((lambda x, y: x * y) ,ModifiedList);
	# ProductList = list(reduce(CalcProduct(ModifiedList), ModifiedList));
	print(ProductList);

if __name__ == "__main__":
	main();