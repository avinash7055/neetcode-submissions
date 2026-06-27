class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        left=0
        s={}
        k=len(s1)
        for i in range(len(s1)):
            s[s1[i]]=s.get(s1[i],0)+1
        f={}
        ans=0
        for right in range(len(s2)):
            f[s2[right]]=f.get(s2[right],0)+1
            if right-left+1>k:
                f[s2[left]]-=1
                if f[s2[left]]==0:
                    del f[s2[left]]
                left+=1
            if s==f:
                return True
            
        return False            
        