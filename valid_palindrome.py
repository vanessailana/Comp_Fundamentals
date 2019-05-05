import string

my_str="Too hot to hoot.".replace(" ", "").strip(string.punctuation).lower();

print(my_str)


rev_str=reversed(my_str);


if list(my_str) == list(rev_str):
    print("It is a palindrome")
    print(my_str[::-1])

else:
    print("Ya right, not a palindrome");