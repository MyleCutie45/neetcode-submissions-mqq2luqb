from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS=len(image),len(image[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        og = image[sr][sc]
        if og == color:
            return image 
        q = deque([(sr,sc)])
        image[sr][sc] = color
        while q:
            r,c=q.popleft()
            for u,v in dirs:
                dr,dc = r+u,c+v
                if 0 <= dr < ROWS and 0 <= dc < COLS and image[dr][dc] == og:
                    image[dr][dc] = color
                    q.append((dr,dc))
        return image
