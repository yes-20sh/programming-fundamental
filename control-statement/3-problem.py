# Write a program to input amount from user and print minimum number of notes (Rs. 500, 100, 50, 20, 10, 5, 2, 1) required for the amount.


amount = int(input("Enter the amount: "))

if amount >= 500:
    print("500 x", amount // 500)
    amount = amount % 500

if amount >= 100:
    print("100 x", amount // 100)
    amount = amount % 100

if amount >= 50:
    print("50 x", amount // 50)
    amount = amount % 50

if amount >= 20:
    print("20 x", amount // 20)
    amount = amount % 20

if amount >= 10:
    print("10 x", amount // 10)
    amount = amount % 10

if amount >= 5:
    print("5 x", amount // 5)
    amount = amount % 5

if amount >= 2:
    print("2 x", amount // 2)
    amount = amount % 2

if amount >= 1:
    print("1 x", amount)