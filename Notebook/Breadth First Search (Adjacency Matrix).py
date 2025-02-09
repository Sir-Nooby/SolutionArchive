#Breadth First Search Algorithm (Adjacency Matrix)

rows = int(input())

columns = int(input())

matrix = [list(input()) for i in range(rows)]

start_row = int(input())

start_col = int(input())

queue = [(start_row, start_col)]

visited = set()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    
    row, column = queue.pop(0)
    
    if (row, column) in visited:
        continue
    
    visited.add((row, column))
    
    print(matrix[row][column])
    
    for i, v in directions:
        new_row, new_column = row + i, column + v
        
        if 0 <= new_row < rows and 0 <= new_column < columns and (new_row, new_column) not in visited:
            queue.append((new_row, new_column))
