def solve():
	nums = [3, 2, 4]
	target = 6
	num_map = {}
	for i, num in enumerate(nums):
		completement = target - num
		if completement in num_map:
			return [num_map[completement], i]
		num_map[num] = i
	
	return []


# Lưu lại vị trí và giá trị đã kiểm tra trước đó
if __name__ == '__main__':
	print(solve())
