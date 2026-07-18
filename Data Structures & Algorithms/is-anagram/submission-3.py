class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s) == len(t):
            visited=[]
            for i in s:
                if i in visited:
                    continue
                
                count1=1
                for j in s:
                    if i==j:
                        count1+=1
                visited.append(i)
                d1[i]=count1-1
            
            visited2=[]
            for i in t:
                if i in visited2:
                    continue
                
                count2=1
                for j in t:
                    if i==j:
                        count2+=1
                visited2.append(i)
                d2[i]=count2-1
            
            for i in d1:
                if i not in d2 or d1[i] != d2[i]:
                    return False
            return True
        else:
            return False


                  