#program to take a string and return the most frequent character in it
#Getting a input from the user
new_str= input('Enter a string:')
#checkingh using count is it is used twice or greater than that
for char in set(new_str):
    if new_str.count(char) >=2 :
        print(char, end=' ')
#if the strings contains only unique character then this statement is printed
else:
        print('The entered string contains unique character only')