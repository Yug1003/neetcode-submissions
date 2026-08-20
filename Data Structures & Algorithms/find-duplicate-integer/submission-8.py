class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = set()

        for i in nums:
            if i in lst:
                return i
            lst.add(i)
