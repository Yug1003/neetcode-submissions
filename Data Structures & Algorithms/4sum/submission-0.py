class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        lst=[]
        visited=[]

        for i in range(n):
            for j in range(i+1 , n):
                for k in range(j+1 , n):
                    for r in range(k+1 , n):
                        if (nums[i] + nums[j] + nums[k] + nums[r] == target):
                            sol = sorted([nums[i], nums[j] , nums[k] , nums[r]])

                            if list(sol) not in visited:
                                visited.append(list(sol))
                                lst.append(sol)

        return lst