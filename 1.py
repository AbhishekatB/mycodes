#find the duplicate number in an array? ie [1,n]

def method1(arr):
	for i in range(0,len(arr)-1):
		count = 0
		for j in range(i,len(arr)):
			if(arr[i]==arr[j]):
				count=count+1
			if(count>1):
				print(arr[i])
				break
	return 0
def method2(arr,temp):
	for i in range(0,len(arr)):
		if(temp[arr[i]]==0):
			temp[arr[i]]=temp[arr[i]]+1
		else:
			print(arr[i])
	return 0
	
def method3(arr):
	slow,fast = arr[0],arr[0]
	while(slow!=fast):
		slow = arr[slow]
		fast = arr[arr[fast]]
	fast = arr[0]
	while(slow!=fast):
		slow = arr[slow]
		fast = arr[fast]
	return slow
	
def main():
	arr = [2,4,5,0,1,5]
	temp = [0]*(max(arr)+1)
	print('method1 complexity is O(n^2)')
	method1(arr)
	print('method2 space complexity = O(n) and Runtime complexity is O(n)')
	method2(arr,temp)
	print(method3(arr))
	return 0
main()

