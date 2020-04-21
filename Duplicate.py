def check_duplicate(inputArray):
	n = max(inputArray)
	temp_arr=[0]*n
	print(temp_arr)
	for i in range(0,n):
		print(inputArray[i],i)
		no = inputArray[i]
		temp_arr[no] += 1

	for i in temp_arr:
		if i > 1 : 
			print (i)

arr =[1,2,3,4]
check_duplicate(arr)