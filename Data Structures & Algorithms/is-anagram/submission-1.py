class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        shash={}
        thash={}
        
        for i in s:
            if i not in shash:
                shash[i]=1
            else:
                shash[i]+=1
        for j in t:
            if j not in thash:
                thash[j]=1
            else:
                thash[j]+=1
        return thash==shash



        