class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        newNum = ''
        i=len(num)-1
        neg = False
        first = True
        
        if (x > ((2**31)-1) or x< -(2**31)):
            return 0
        
        while(i>=0):
            if(num[i]=='-'):
                neg = True
                i -=1
                continue
            if(num[i]=='0' and first and i>0):
                i -=1
                continue
            else:
                newNum += num[i]
                first = False
                i -=1
        
        if (int(newNum) > ((2**31)-1) or int(newNum) < -(2**31)):
            return 0
        
        if(neg):
            return -1* int(newNum)
        else:
            return int(newNum)
        