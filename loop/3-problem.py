# Write a program to input number from user and check number is palindrome or not using loop. 

num = input("Enter the number : ")

isPalindrome =  False

for i in range(len(num) // 2):
    if num[i] == num[len(num) - i - 1]:
        isPalindrome = True
    else: 
        isPalindrome = False
        break
if isPalindrome:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
