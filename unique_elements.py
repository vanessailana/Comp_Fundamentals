import collections;
import heapq;

def topKFreq(self,nums,k):


     count=collections.Counter(nums);

     return [x[0] for x in c.most_common(k)] ;



