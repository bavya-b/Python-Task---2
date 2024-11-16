#program that takes a string, remove vowels in the string and display the string
#getting a input from the user
String_to_remove_vowels= input('Enter any string to remove vowels:')
#Replace each vowel with a space
var_remove_a= String_to_remove_vowels.replace("a", "")
var_remove_e= var_remove_a.replace ("e", "")
var_remove_i= var_remove_e.replace("i", "")
var_remove_o= var_remove_i.replace("o", "")
var_remove_u= var_remove_o.replace("u", "")
#Printing the vowel removed string
print(f'The Entered string without vowels is {var_remove_u}')
