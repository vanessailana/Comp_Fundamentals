


def maxSum(a,size):
    max_so_far=a[0];
    curr_max=a[0];

    for i in range(1,size):
        curr_max=max(a[i], curr_max+a[i]);
        max_so_far=max(max_so_far,curr_max);

    return max_so_far;



a = [-5,-1,-8,-9] 
print(maxSum(a,len(a)))


##
# Function to find the maximum contiguous subarray 
# and print its starting and end index 


