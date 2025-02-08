#Problem J5: Harvest Waterloo - 2024 (SirNooby)
rows = int(input())
columns = int(input())

patch = [list(input()) for i in range(rows)]

starting_row = int(input())
starting_column = int(input())

queue = [(starting_row, starting_column)]

visited = set()

total = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    row, column = queue.pop(0)
    
    if (row, column) in visited:
        continue
    
   
    visited.add((row, column))
    
    if patch[row][column] == "S":
        total += 1
    elif patch[row][column] == "M":
        total += 5
    elif patch[row][column] == "L":
        total += 10
    else:
        pass
    
    for i, v in directions:
        new_row, new_column = row + i, column + v 
        
        if 0 <= new_row < rows and 0 <= new_column < columns and patch[new_row][new_column] != "*" and (new_row, new_column) not in visited:
            queue.append((new_row, new_column))

print(total)
