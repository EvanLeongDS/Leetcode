class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #final solution
        big_list = []
        pacific_set = set()
        atlantic_set = set()
        # loop through the perimeter of the grid
        # m: row count, n is column count
        m, n = len(heights), len(heights[0])

        # iterate through the outer cells of pacific ocean and atlantic ocean
        for i in range(m):
            self.dfs(heights, i, 0, pacific_set)
        for j in range(n):       
            self.dfs(heights, 0, j, pacific_set)
        for i in range(m):
            self.dfs(heights, i, n-1, atlantic_set)
        for j in range(n):       
            self.dfs(heights, m-1, j, atlantic_set)
        
        # compare the two sets and keep the combine one into intersected_set:
        for pair in pacific_set: 
            if pair in atlantic_set:
                small_list = [pair[0], pair[1]]
                big_list.append(small_list)

        # sort the big list
        big_list.sort()
        return big_list


    def dfs(self, heights, i , j, ocean_set):
        ocean_set.add((i, j))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for direction in directions:
            newx = i + direction[0]
            newy = j + direction[1]

            # make sure its in range, not in the set, and is greater than the current x 
            if 0 <= newx <= len(heights) -1 and 0 <= newy <= len(heights[0]) - 1 and (newx, newy) not in ocean_set and heights[newx][newy] >= heights[i][j]:
                # add to the newset
                ocean_set.add((newx, newy))
                self.dfs(heights, newx, newy, ocean_set)
