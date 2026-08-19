class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited=[]
        l=0

        for i in nums:
            if i not in visited:
                visited.append(i)
                nums[l]=i
                l+=1

        return l