new_str= input('Enter a string:')
for char in set(new_str):
    if new_str.count(char) == 1:
        print(char, end=' ')