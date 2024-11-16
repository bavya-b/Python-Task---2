#Program that takes a string and display TRUE if it a palindrome of another string or else False
#Getting a input for string 1
String_1 = input ('Enter a value for string 1:')
#capitalize string_1
Cap_String_1= String_1.upper()
#Getting a input for string 2
String_2 = input ('Enter a value for string 2:')
#capitalize string_2
Cap_String_2= String_2.upper()
#reversing the cap.String_2
String_3 = Cap_String_2[::-1]
# Verify if the string_1 is a palindrome of string_2
print (Cap_String_1==String_3)