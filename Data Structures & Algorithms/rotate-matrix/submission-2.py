from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left,right=0,len(matrix)-1
        while left<right:
            for i in range(right-left):
                top,bot=left,right 
                topleft = matrix[top][left+i]
                matrix[top][left+i]=matrix[bot-i][left]
                matrix[bot-i][left]=matrix[bot][right-i]
                matrix[bot][right-i]=matrix[top+i][right]
                matrix[top+i][right]=topleft
            left += 1
            right -= 1
                
