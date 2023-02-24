def FloodFill(image:list[list[int]],sr,sc,new_color):
    curr_color = image[sr][sc]
    row = len(image)
    col = len(image[0])

    def dfs(sr,sc):
        if 0<=sr<row and 0<=sc<col and image[sr][sc]==curr_color and image[sr][sc]!=new_color :
            image[sr][sc] = new_color
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)

    dfs(sr,sc)

    return image

print(FloodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))