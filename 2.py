# 0,1,2 sequence sort them
# counting sort O(2*N)
# Dutch flag algorithm O(N)
# low,mid,high
# all elements left of low are 0, right of high are 2

class Solution:    
    def DNFA(self,arr):
        low = 0
        n = len(arr)
        high = len(arr)-1
        mid = 0
        while(mid<=high):
            if(arr[mid]==0):
                arr[low],arr[mid] = arr[mid],arr[low]
                low = low+1
                mid = mid+1
            elif(arr[mid]==1):
                mid=mid + 1
            elif(arr[mid]==2):
                arr[mid],arr[high] = arr[high],arr[mid]
                high = high - 1 
        print(arr)
    def quicksort(self,arr):
        pass
    def countingsort(self,arr):
        
arr = [0,1,0,2,1,0,0,0,1,1,1,2,0,0]
Solution().DNFA(arr)
