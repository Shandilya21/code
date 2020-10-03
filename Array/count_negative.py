class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = []
        for val in range(len(grid)):
            for res in range(len(grid[val])):
                if grid[val][res] < 0:
                    total.append(1)
        
        return sum(total)