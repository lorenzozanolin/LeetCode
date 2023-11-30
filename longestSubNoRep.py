class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            temp = self.prefCalc(self,s[i:])
            if max < temp: 
                max = temp
        return max
        
    def prefCalc(self,s):
        i = 0
        pref = ""
        while i<len(s):    #while the string is not empty
            if(s[i] not in pref):
                pref += s[i]
                i += 1
            else:
                break
        print(pref)
        return i
    
    
print(Solution.lengthOfLongestSubstring(Solution,"pwwkew"))