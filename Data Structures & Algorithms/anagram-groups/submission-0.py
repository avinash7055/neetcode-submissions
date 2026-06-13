class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s1={}
        
        for s in strs:
            
            key="".join(sorted(s))
            if key not in s1:
                s1[key]=[]

            s1[key].append(s)    
            
        return list(s1.values())