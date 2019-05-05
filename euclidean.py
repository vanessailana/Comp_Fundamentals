import numpy as np
from scipy.stats import pearsonr
def euclidean(v1,v2):
    v1=np.array(v1);
    v2=np.array(v2);
    diff=np.power(np.array(v1)-np.array(v2),2)
    sigma_value=np.sum(diff);
    euclid_score=np.sqrt(sigma_value)
    return euclid_score;




v1=[1,2,3,41,1]
v2=[2,1,2,3,1]

print(euclidean(v1,v2))
#eucliden distance failed 



#pearson correlation goes between -1 and 1 

alice=[1,1,3,2,4]
bob=[2,2,4,3,5]

print(euclidean(alice,bob));

#correlated 

print(pearsonr(alice,bob))
#highest possbile similarity score 