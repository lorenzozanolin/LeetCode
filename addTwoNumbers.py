class Solution:
    def addTwoNumbers(self, l1, l2):
        value = self.getValue(l1) + self.getValue(l2) 
        finalList = []
        i = 0
        while (value != 0):
            digit = int(value % 10)
            finalList.insert(i,digit)
            value = (value - digit) / 10
            i +=1
        return finalList   
        
    def getValue(self,l):
        val = 0
        i=0
        while (i != len(l)):
            val += (10**i)*l[i]
            i += 1
        return val 
    