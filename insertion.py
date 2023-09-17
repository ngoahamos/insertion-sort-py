
def insertionSort(arr):
	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
		print("Pass " + str(i))
		print(arr)



data = input("Enter numbers separated by commas: ");
try:
    arr = list(map(lambda a: int(a) , data.split(',')))
    print("input data")
    print(arr)
    insertionSort(arr)
except Exception as e:
	print(f"Error Occured: {e}")



