def solve():
	nums = [1, 12, -5, -6, 50, 3]
	nums = [5]
	nums = [0, 4, 0, 3, 2]
	nums = [4, 2, 1, 3, 3]
	k = 2
	j = k
	i = 0
	check = sum(nums[:k])
	res = check
	while j < len(nums):
		check = check - nums[i] + nums[j]
		res = max(res, check)
		j += 1
		i += 1
	
	return res / k


if __name__ == "__main__":
	print(solve())
