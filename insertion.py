# insertion sort function 
def insertionSort(arr):
	#run through the list
	for i in range(1, len(arr)):
		# key pointer
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				# perform swap
				arr[j + 1] = arr[j]
				j -= 1
		# update key
		arr[j + 1] = key
		# print pass
		print("Pass " + str(i))
		# print input data at specific pass 
		print(arr)
# get input from user
data = input("Enter numbers separated by commas: ");


try:
    arr = list(map(lambda a: int(a) , data.split(',')))
    print("input data")
    print(arr)
    insertionSort(arr)
except Exception as e:
	print(f"Error Occured: {e}")



