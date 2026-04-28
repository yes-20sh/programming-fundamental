# Write a program to input two numbers from user and find maximum between two numbers using switch case.

num1 , num2 = map(int, input("Enter the number-1 and number-2 : ").split())

match num1 > num2:
    case True:
        print(num1)
    case False:
        print(num2)