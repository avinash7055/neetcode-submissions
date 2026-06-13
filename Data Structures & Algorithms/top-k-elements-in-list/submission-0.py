class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for num in nums:
            s[num]=s.get(num,0)+1
        d=sorted(s.items(), key=lambda item:item[1],reverse=True)
        
        l=[]
        for i in range(k):
            l.append(d[i][0])
            
                
        return l



        