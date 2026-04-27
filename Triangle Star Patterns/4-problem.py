'''
    *
   **
  * *
 *  *
*****
'''

rows = int(input("Enter the number of rows: "))

for row in range(rows):
    for column in range(rows):
        if column == rows - 1 or column == rows - row - 1 or  row == rows -1:
            print("*", end="") 
        else:
            print(" ", end="")
    print()

