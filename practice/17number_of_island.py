# graph leetcode problem


# given a 2D grid where 1 represents land and 0 represents water. count and return the number of islands.
# and island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water . you may assume
# the grid is surrounded by water (i.e all the edges are water.)



input_grid = [
    ['0','1','1','1','0'],
    ['0','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0',"1",'0']
]





def num_of_islands(grid):
    islands = 0
    visited  = set()
    rows, cols = len(grid), len(grid[0])
    
    #all the direction we can go to bfs
    moves = [(-1,0),(1,0), (0,-1), (0,1)]
    
    # loop through every cell
    for row in range(rows):
        for col in range(cols):
            val = grid[row][col]
            #'0' for water, '1' for land
            if val == '0' or (row,col) in visited:
                #skip these cells they are either water or already visited
                continue
                
            #we found island
            islands +=1
            queue = [(row,col)]
            
            while len(queue) > 0:
                pop_row, pop_col = queue.pop(0)
                visited.add((pop_row,pop_col))
                #get neighbours
                for drow, dcol in moves:
                    neighbour_row, neighbour_col = pop_row + drow, pop_col + dcol
                    # is this a valid neighbour
                    #off the grid
                    if neighbour_row < 0 or neighbour_row>=rows:
                        continue
                    if neighbour_col < 0 or neighbour_col>=cols:
                        continue
                    
                    #skip water and visited cells
                    if grid[neighbour_row][neighbour_col] == "0":
                        continue
                    
                    if (neighbour_row, neighbour_col) in visited:
                        continue
                    queue.append((neighbour_row, neighbour_col))
    return islands


print(num_of_islands(input_grid))