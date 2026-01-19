def solve():
	s = "abcabcbb"
	# s = "pwwkew"
	# s = "au"
	# s = "dvdf"
	map = set()
	L = 0
	res = 0
	for R in range(len(s)):
		while s[R] in map:
			map.remove(s[L])
			L += 1
		
		map.add(s[R])
		res = max(res, R - L + 1)
	
	return res
	# print(map)
	return res


# Loại bỏ tất cả những kí tự bị lặp ở phía sau
# Dùng set vì nó hỗ trợ hàm xóa kí tự dễ hàng hơn dùng list thông thường
if __name__ == "__main__":
	print(solve())
