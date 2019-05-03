
char=256

def longestSub(string):
    n=len(string)
    cu=1;
    max=1;
    pre,i=0;

    visited=[-1]*char

    #mark the first character as visited 
    visited[ord(string[0])] = 0

     # then do cur_len++ 
    if pre== -1 or (i - cur > pre): 
        cu+=1
    else: 
        if cur> max: 
                max = cur
  
        cur = i - pre
  
        # update the index of current character 
        visited[ord(string[i])] = i 
  
    # Compare the length of last NRCS with max_len and update 
    # max_len if needed 
    if cur > max: 
        max = cur 
  
    return max;