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
    def Selectionsort(self,arr,n):
        for i in range(0,n):
            imin = i
            for j in range(i+1,n):
                if(arr[imin]>arr[j]):
                    imin = j
            arr[imin],arr[i]=arr[i],arr[imin]
        print(arr)
        return arr
    def Insertionsort(self,arr,n):
        for i in range(1,n):
            hole = i
            value = arr[hole]
            while(hole>0 and arr[hole-1]>value):
                #arr[hole-1],arr[hole]= arr[hole],arr[hole-1] this also works but for complexity issues not cosidered
                arr[hole] = arr[hole-1]
                hole = hole-1
            arr[hole] = value
        print(arr)
        return arr
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

arr = [9,5,2,6,4,1,3,100,56,89]
n = len(arr)
Sorting().Insertionsort(arr,n)
Sorting().Bubblesort(arr,n)
Sorting().Selectionsort(arr,n)

