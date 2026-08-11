class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a > 0x7fffffff:
            a -= 0x100000000

        return a