A = [1,2,3,5,3,2,1,4]
dist = list(set(A))
occurences = [0]*len(A)
s = []
for i in range(0,len(dist)):
	c = 0
	for j in range(0,len(A)):
		if(A[j]==dist[i]):
			c =c +1
	occurences[i]=c
for i in range(0,len(occurences)):
	if(occurences[i]==1):
		s.append(dist[i])
print(sum(s))
'''
# Quicksort
A = [2,4,1,6,8,5,3,7]
# find the position of pivot using partition
# pivot as last element
def partition(l,h):
	pivot = A[h]
	pindex = l
	for i in range(l,h):
		if(A[i]<=pivot):
			A[i],A[pindex]=A[pindex],A[i]
			pindex = pindex +1
	A[pindex],A[h]=A[h],A[pindex]
	return pindex
def Quicksort(l,h):
	if(l<h):
		j = partition(l,h)
		Quicksort(l,j-1)
		Quicksort(j+1,h)
Quicksort(0,len(A)-1)

print(A)


2,4,1,6,8,5,3,7
0,1,2,3,4,5,6,7

pindex = 4
i=5
2,4,1,6,5,8,3,7
0,1,2,3,4,5,6,7
pindex = 5
i=6
2,4,1,6,5,3,8,7
0,1,2,3,4,5,6,7
pindex = 6
i=6



# 2,4,1,6,8,5,3,7
# merge_sort(R)
# merge_sort(L)
# merge(L,R,A)

A = [2,4,1,6,8,5,3,7]
graph = []

def merge(L,R,A):
	nL = len(L)
	nR = len(R)
	i=j=k=0
	while(i<nL and j<nR):
		if(L[i]<=R[j]):
			A[k]=L[i]
			i=i+1
		else:
			A[k]=R[j]
			j =j+1
		k=k+1
	while(i<nL):
		A[k]=L[i]
		i=i+1
		k=k+1
	while(j<nR):
		A[k]=R[j]
		j=j+1
		k=k+1

def merge_sort(A):
	n = len(A)
	if(n<2):
		return 0
	mid = int(n/2)
	L = [0]*mid
	R = [0]*(n-mid)
	for i in range(0,mid):
		L[i]=A[i]
	for i in range(0,n-mid):
		R[i]=A[mid+i]
	merge_sort(L)
	merge_sort(R)
	merge(L,R,A)
	
merge_sort(A)
print(graph)
print(A)

'''