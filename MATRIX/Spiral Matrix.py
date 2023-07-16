"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        top,left=0,0
        right=len(matrix[0])
        bottom=len(matrix)
        while(left<right and top<bottom):
            for i in range(left,right):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            right-=1
            if left<right and top<bottom:
                for i in range(right-1,left-1,-1):
                    ans.append(matrix[bottom-1][i])
                bottom-=1
                for i in range(bottom-1,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans
"""
Above is the only and the optimal solution to this problem.
The concept is to print the matrix in a spiral order.
