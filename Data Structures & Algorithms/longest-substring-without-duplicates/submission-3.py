class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[l])
                l+=1

            c.add(s[i])
            res= max(res , i-l+1)
        return res
