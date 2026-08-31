class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        count = 0
    
        for i in nums:
            count |= i

        return count << (len(nums)-1)
