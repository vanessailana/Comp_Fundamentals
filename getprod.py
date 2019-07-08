
def prodArray():

    array=[10,3,5,6,2]
    n=len(array);

    i,temp=1,1

    prod=[1 for i in range(n)]

    #products from the left 
    for i in range(n):
        prod[i]=temp
        temp*=array[i];


    temp=1;


    for i in range(n-1,-1,-1):
        prod[i]*=temp
        temp*=array[i];

    for i in range(n):
        print(prod[i],end="  ")

    return;




print(prodArray())