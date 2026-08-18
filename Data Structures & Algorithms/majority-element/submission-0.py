class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        m=0
        ans=0
        for i in nums:
            d[i]=d.get(i,0)+1

            if d[i]>m:
                m=d[i]
                ans=i
        return ans
        