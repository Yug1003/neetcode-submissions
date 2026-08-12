class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]
        for i in operations:
            if i=='+':
                lst.append(lst[-1]+lst[-2])
            elif i=='C':
                lst.remove(lst[-1])
            elif i=='D':
                lst.append(lst[-1]*2)
            else:
                lst.append(int(i))
        return sum(lst)