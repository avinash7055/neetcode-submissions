class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        f={}
        m_f=0
        ans=0
        for right in range(len(s)):
            f[s[right]]=f.get(s[right],0)+1
            m_f=max(f.values())
            while (right-left+1)-m_f>k:
                f[s[left]]-=1
                left+=1

            ans=max(ans,right-left+1)
        return ans        
        