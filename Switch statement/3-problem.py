# Write a program to input number from user and check whether the number is even or odd using switch case.

num = int(input("Enter the number: "))

match num % 2 == 0:
    case True:
        print(f"{num} is even number")
    case False:
        print(f"{num} is odd number")