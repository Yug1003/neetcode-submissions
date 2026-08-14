class Solution:
    def isValid(self, s: str) -> bool:
        m= {')':'(', '}':'{' , ']':'['}
        lst=[]

        for i in s:
            if i in m:
                top= lst.pop() if lst else '#'

                if m[i]!= top:
                    return False
                
            else:
                lst.append(i)
        
        return not lst