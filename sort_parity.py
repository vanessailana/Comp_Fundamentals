def sortParity(self,A):

    even=[]
    odd=[]

    for number in A:
        if number%2:
            odd.append(number);
        else:
            even.append(number);

    return even+odd;