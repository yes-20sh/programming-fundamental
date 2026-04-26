# Write a program to input a character from user and check whether given character is alphabet, digit or special character.

character = input("Enter the character : ")

if character.isdigit:
    print(f"{character} is digit")
    
elif character.isalpha:
    print(f"{character} is alphabet")

elif character.isalnum():
    print(f"{character} is Alphanumeric")
else:
    print(f"{character} is special character")