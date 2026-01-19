def solve():
	nums = [2, 0, 2, 1, 1, 0]
	# nums = [2, 0, 1]
	nums = [1, 0, 1]
	
	i = 0
	j = len(nums) - 1
	while j > i:
		if nums[i] == 1 and nums[j] == 1:
			j -= 1
		if nums[i] != 0:
			temp = nums[i]
			nums[i] = nums[j]
			nums[j] = temp
		if nums[i] == 0:
			i += 1
		if nums[j] == 2:
			j -= 1
		
		print(nums, i, j)
	return nums


if __name__ == "__main__":
	print(solve())
