class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left=0
        # window=set()
        # ans=0
        # for right in range(len(s)):
            
        #     while s[right] in window:
        #         window.remove(s[left])
        #         left+=1

        #     window.add(s[right])

        #     ans =max(ans,right-left+1)
        # return ans     

        f={}
        ans=0
        left=0
        for right in range(len(s)):
            f[s[right]]=f.get(s[right],0)+1

            while f[s[right]]>1:
                f[s[left]]-=1
                if f[s[left]]==0:
                    f.pop(s[left])
                left+=1
            ans=max(ans,right-left+1)    

        return ans    
