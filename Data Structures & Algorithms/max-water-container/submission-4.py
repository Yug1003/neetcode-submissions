class Solution:
    def maxArea(self, heights: List[int]) -> int:
        count=1
        lst=[]

        for i in range(len(heights)):
            for j in range(i+1 , len(heights)):
                res= min(heights[i] , heights[j])
                c = j-i
                res= res*c
                lst.append(res)

        return max(lst)