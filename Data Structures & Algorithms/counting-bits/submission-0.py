class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            bi = bin(i).count('1')
            lst.append(bi)
        return lst