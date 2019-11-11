from functools import *;

def Acceptdata():
    arr_list = list();
    n = int(input("Enter Number of Elements : "));
    for i in range(0,n):
        print("Please enter number ", i+1);
        element = int(input());
        arr_list.append(element);
    return arr_list;

def main():
    userdata = Acceptdata();
    print(userdata);
    FilterData = list(filter(lambda x: (x % 2 == 0),userdata));
    print(FilterData);
    ModifiedData = list(map(lambda x:(pow(2,x)),FilterData));
    print(ModifiedData);
    Finaldata = reduce(lambda x,y: (x + y), ModifiedData);
    print(Finaldata);

if __name__ == "__main__":
    main();