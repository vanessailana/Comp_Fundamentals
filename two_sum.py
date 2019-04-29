#given 
# an array of integers 
# return indices and sum of the unoque target


def twoSum(nums,target):
        dic={}
        length=len(nums)
        for i in range(0,length):
                val=nums[i];
                if (target - val) in dic:
                        return (dic[target - val], i + 1)
                dic[val] = i + 1



                


num=[2, 7, 11, 15]
t= 9
print (twoSum(num, t))





