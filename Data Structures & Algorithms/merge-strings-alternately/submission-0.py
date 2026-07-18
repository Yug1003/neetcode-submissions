class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        w1=[]
        w2=[]

        for i in word1:
            w1.append(i)

        for j in word2:
            w2.append(j)

        if len(word1)>len(word2):
            count=0
            for i in range(len(word2)):
                res+=w1[i]
                res+=w2[i]
                count=i
            
            count+=1
            for i in range(count,len(word1)):
                res+=w1[i]

        elif len(word2)>len(word1):
            count=0
            for i in range(len(word1)):
                res+=w1[i]
                res+=w2[i]
                count=i
            
            count+=1
            for i in range(count,len(word2)):
                res+=w2[i]

        if len(word1)==len(word2):
            for i in range(len(word2)):
                res+=w1[i]
                res+=w2[i]

        return res