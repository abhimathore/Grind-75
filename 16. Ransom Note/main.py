class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapp = {}
        
        for i in ransomNote:
            if i not in mapp:
                mapp[i] = 1
            else:
                mapp[i] +=1
            
        for i in magazine:
            if i in mapp:
                mapp[i] -=1
                if mapp[i] == 0:
                    del[mapp[i]]
                if len(mapp) == 0:
                    return True
        return False