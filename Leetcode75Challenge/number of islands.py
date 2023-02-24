def numIslands(grid):
    # Edge case: empty grid
    if not grid:
        return 0

    # Initialize variables
    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(grid, i, j):
        # Base cases: out of bounds or current cell is not an island
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return

        # Mark the current cell as visited
        grid[i][j] = '0'

        # Recursively visit the cells above, below, to the left, and to the right
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    # Iterate through the grid and call dfs() on each island cell
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count

print(numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))