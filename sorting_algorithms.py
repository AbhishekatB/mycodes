class Sorting:
    def Bubblesort(self,arr,n):
        for i in range(1,n):
            flag = 0
            for j in range(0,n-i):
                if(arr[j+1]<arr[j]):
                    arr[j+1],arr[j] = arr[j],arr[j+1]
                    flag = 1
            if(flag==0):
                break
        print(arr)
        return arr
    def Insertionsort(self,arr):
        pass
    def Selectionsort(self,arr):
        pass
    def Mergesort(self,arr):
        pass
    def Quicksort(self,arr):
        pass
    def Countingsort(self,arr):
        pass
    def Timsort(self,arr):
        pass
    def Gapsort(self,arr):
        pass
    def Radixsort(self,arr):
        pass
arr = [9,5,2,6,4,1,3]
Sorting().Bubblesort(arr,len(arr))
