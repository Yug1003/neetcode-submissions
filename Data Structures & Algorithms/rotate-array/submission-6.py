class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        lst=[]
        for i in range(len(nums)-k , len(nums)):
            lst.append(nums[i])

        for i in range(0 , len(nums)-k):
            lst.append(nums[i])
        
        nums[:] = lst