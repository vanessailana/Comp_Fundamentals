my_str='adffsdsddsf';

my_str=my_str.casefold();

#reverse a string 

rev_str=reversed(my_str);


if list(my_str) == list(rev_str):
    print("It is a palindrome")

else:
    print("Ya right, not a palindrome");