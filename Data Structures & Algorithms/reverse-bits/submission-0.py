class Solution:
    def reverseBits(self, n: int) -> int:
        raw= bin(n)[2:]
        z = raw.zfill(32)
        z1= z[::-1]
        return int(z1 , 2)