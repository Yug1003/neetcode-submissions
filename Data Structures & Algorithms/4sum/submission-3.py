from bisect import bisect_left

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = []
        seen = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):

                    fourth = target - (nums[i] + nums[j] + nums[k])

                    idx = bisect_left(nums, fourth, k + 1)

                    if idx < n and nums[idx] == fourth:
                        quad = (nums[i], nums[j], nums[k], nums[idx])

                        if quad not in seen:
                            seen.add(quad)
                            ans.append(list(quad))

        return ans