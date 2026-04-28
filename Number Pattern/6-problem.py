'''
1
12
123
1234
12345

'''

rows = int(input("Enter the number of rows: "))

for row in range(1, rows + 1):
    for column in range(1, row + 1):
        print(column, end="")
    print()
