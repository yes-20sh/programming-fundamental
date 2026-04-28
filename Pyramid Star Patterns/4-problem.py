'''
*********
 *     *
  *   *
   * *
    *
'''

rows = int(input("Enter the number of rows: "))

for row in range(rows, 0, -1):
    for column in range(2 * rows - 1):
        
        if row == rows or column == (rows - row) or column == (rows + row - 2):
            print("*", end="")
        else:
            print(" ", end="")
    
    print()