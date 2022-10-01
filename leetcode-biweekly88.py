class Solution:
    def equalFrequency(self, word: str) -> bool:
        d={} # frequency of charaters
        for w in word:
            d[w]=d.get(w,0)+1
            
        if len(d)==1 or max(list(d.values()))==1:# for cases like abcd=[1,1,1,1] or aaaa=[4]
            return True
        
        freq_=d.values()
        freq=dict()# frequency of frequency of character
        
        for f in freq_:
            freq[f]=freq.get(f,0)+1
        print(freq)
        
        if len(freq)==2:
            temp1,temp2=list(freq.keys())
            k2=temp1 if temp1>temp2 else temp2
            k1=temp1+temp2-k2
            # above pulled k2 as bigger and k1 as smaller dont worry about it...
            
            if k2-k1==1:
                if freq[k2]==1:# for cases like aaccbbb=[2,2,3]
                    return True
                if freq[k1]==1 and k1==1:# for cases like abbccdd=[1,2,2,2]
                    return True
        return False
            
        
        
            
        
