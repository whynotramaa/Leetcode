class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # initialize and populate grid
        row, cols = len(grid), len(grid[0])
        q = deque() # we will be having rows, cols in queue and nth else so remember that
        fresh_count = 0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # define var like minutes and directions
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS Traversal
        # get r, c from q and nr, nc from directions + row and col
        # if nr nc are in boundaries and grid[nr][nc] == 1 that is fresh make it = 2 and fresh-=1
        # also apppend it to queue as it is a rotten one now
        # and after for loop finishes, time+=1
        while q:
            rotted = False
            for _ in range(len(q)): #bcz we need to finish all neighbors of prev oranges 
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<row and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_count -= 1 
                        q.append((nr,nc))
                        rotted = True
            if rotted == True:
                minutes+=1

        return minutes if fresh_count == 0 else -1 
