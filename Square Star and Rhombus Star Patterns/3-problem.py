'''
*****
** **
* * *
** **
*****
'''

rows = int(input("Enter the number of row: "))

for row in range(rows):
    for column in range(rows):
        if (row == 0 or row == rows - 1 or 
            column == 0 or column == rows - 1 or 
            row == column or row + column == rows - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()