#program to calculate total number and count of each vowels in the string
#defining the given string into a variable
String= "Guvi Geeks Network Private Limited"
#counting the number of each vowel in the string
a= String.count('a')
print(f'The number of Vowel "a" in the string is: {a}')
e= String.count('e')
print(f'The number of Vowel "e" in the string is: {e}')
i= String.count('i')
print(f'The number of Vowel "i" in the string is: {i}')
o= String.count('o')
print(f'The number of Vowel "o" in the string is: {o}')
u= String.count('u')
print(f'The number of Vowel "u" in the string is: {u}')
#Finding the sum of all the vowels in the string
sum = a+e+i+o+u;
print(f'The total number of vowels in the string is {sum}')