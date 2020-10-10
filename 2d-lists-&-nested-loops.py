#two dimentional lists 

#inside number_grid list there are four elements which themselves are lists.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#prints the first index of the first array.
print(number_grid[0][0])

#prints the second index of the third array.
print(number_grid[2][1])

#how to parse thru a two dementional array
for row in number_grid: 
    for col in row:  
        print(col)
    
    
