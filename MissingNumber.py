def main(arr):
	inp_sum = sum(arr)
	total=0
	for i in range(1,11):
		total += i

	print(inp_sum,total)
	diff = total - inp_sum
	return diff


arr = [1,2,3,4,5,6,8,9,10]
print('Missing Number is',main(arr))