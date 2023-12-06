class Solution:
    def myAtoi(self, s: str) -> int:
        found = 0
        x=0
        index1 = -1
        index2 = -1
        l = len(s)
        while found!=1 and x<l: 
            c = s[x]
            if ((c.isdigit() and c!=0) or c=='-'):
                found=1
                index1 = x
                #x+=1
            if c.isalpha():
                return 0
            else:
                x+=1

        while found != 0 and x<l:
            c = s[x]
            if not c.isdigit():
                found = 0
                index2 = x-1
            else:
                x += 1
                if x==l:
                    index2 = x
                    found=0

        num = s[index1:index2+1]
        
        
        if (-2**31<=int(num)<=(2**31)-1):
            return int(num) 
        if (int(num)>(2**31)-1):
            return (2**31)-1
        else:
            return -2**31


print(Solution.myAtoi(Solution,"42"))