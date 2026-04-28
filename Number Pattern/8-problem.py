'''
56789
4567
345
23
1
'''

rows = int(input("Enter the number of rows: "))

for row in range(rows, 0, -1):
    for column in range(row):
        print(row+ column, end="")
    print()