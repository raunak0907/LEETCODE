class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        l,r=0,cols-1
        while l<=r:
            mid=(l+r)//2
            max=0
            for i in range(rows):
                if mat[i][mid]>mat[max][mid]:
                    max=i
            left=mat[max][mid-1]if mid>0 else-1
            right=mat[max][mid+1]if mid<cols-1 else-1

            if mat[max][mid]>left and mat[max][mid]>right:
                return(max,mid)
            elif left>mat[max][mid]:
                r=mid-1
            else:
                l=mid+1
        