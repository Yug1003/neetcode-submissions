class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        
        for _ in range(count):
            nums.remove(val)
        
        rem = len(nums)
        return rem