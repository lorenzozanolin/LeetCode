class Solution:
    def mergeSort(self,arr):
        if len(arr) > 1:

            # Finding the mid of the array
            mid = len(arr)//2

            # Dividing the array elements
            L = arr[:mid]

            # Into 2 halves
            R = arr[mid:]

            # Sorting the first half
            self.mergeSort(L)

            # Sorting the second half
            self.mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def binarySearch(self,arr, low, high, x):
        # Check base case
        if high >= low:
    
            mid = (high + low) // 2
    
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binarySearch(arr, low, mid - 1, x)
    
            # Else the element can only be present in right subarray
            else:
                return self.binarySearch(arr, mid + 1, high, x)
    
        else:
            # Element is not present in the array
            return -1
                

    def twoSum(self,nums,target):
        original = nums.copy()
        self.mergeSort(nums)
        found = False
        couple = []
        i1=0
        taken=-1
        while not found:
            i2 = self.binarySearch(nums,0,len(nums)-1,target-nums[i1])
            if i2 != -1:
                if (nums[i1] != nums[i2]):
                    couple.append(original.index(nums[i1]))
                    couple.append(original.index(nums[i2]))
                else:
                    taken = original.index(nums[i1])
                    couple.append(taken)
                    couple.append(original.index(nums[i1],taken+1))
                found = True
            else:
                i1 +=1
        return couple