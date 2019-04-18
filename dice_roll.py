import random
from collections import Counter;


min=1;
max=6;

def rollDice():
    numberOfRolls=int(input("how many times would you like to  roll the dice"));
    count=numberOfRolls;


    while numberOfRolls >= count and count > 0:

        lst=random.randint(min,max);
        
     

        print(lst);


        count=count-1;
  
        
        







rollDice();

