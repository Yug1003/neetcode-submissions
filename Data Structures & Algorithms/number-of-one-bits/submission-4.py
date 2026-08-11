class Solution:
    def hammingWeight(self, n: int) -> int:
        num= bin(n)
        count=0
        for i in num:
            if i=='1':
                count+=1
        return count