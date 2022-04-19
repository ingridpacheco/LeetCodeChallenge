class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        mod = len(grid) * len(grid[0])
        
        if k == 0 or k%mod == 0:
            return grid
        
        move = k%mod
        columns = len(grid[0])
        moving_numbers = move%columns
        moving_lines = int(move/columns)
        
        if moving_numbers == 0:
            return grid[len(grid) - moving_lines:] + grid[:len(grid) - moving_lines]
        
        new_grid = [[] for k in range(len(grid))]
        
        for i in range(len(grid) - 1, -1, -1):
            
            new_numbers = grid[i][-moving_numbers:]
            new_line = (i + moving_lines) % len(grid)
            
            if len(new_numbers) != columns:
                old_numbers = grid[i][:-moving_numbers]
                new_grid[new_line] = old_numbers + new_grid[new_line] if i != 0 else new_grid[new_line] + old_numbers
                new_line = (new_line + 1) % len(grid)
                new_grid[new_line] = new_numbers + new_grid[new_line]
            else:
                new_grid[new_line] = new_numbers + new_grid[new_line]
            
        return new_grid