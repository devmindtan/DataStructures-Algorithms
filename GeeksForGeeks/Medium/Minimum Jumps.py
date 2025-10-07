# C1
def minJumps_c1(arr):
    check = 0
    res = 0
    index = 0
    dis = arr[0]
    if (arr[0] == 0):
        return -1
    if (arr[0] == len(arr) - 1 or arr[0] > len(arr)):
        return 1
    for i in range(len(arr)):
        if (index == 0):
            dis = arr[i]
            check += 1
        if (res < len(arr) - 1):
            check += 1
            dis = arr[index] + index

        for j in range(index, dis + 1):
            sum = arr[j] + j
            if (sum > res):
                res = sum
                index = j
        if (res >= len(arr) - 1 and check < len(arr)):
            return check
        elif (res <= len(arr) - 1 and check >= len(arr)-1):
            return -1
    return check


# C2
def minJumps_c2(arr):
    n = len(arr)
    if n == 0:
        return -1        # không có phần tử
    if n == 1:
        return 0         # đã ở cuối
    if arr[0] == 0:
        return -1        # không thể di chuyển từ đầu

    jumps = 0            # số nhảy đã dùng
    current_end = 0      # biên phải của phạm vi hiện tại
    furthest = 0         # vị trí xa nhất có thể vươn tới từ phạm vi hiện tại

    # duyệt đến n-2 đủ (vì nếu đã ở n-1 thì không cần xét)
    for i in range(n - 1):
        # mở rộng phạm vi khả dụng
        if i + arr[i] > furthest:
            furthest = i + arr[i]

        # nếu đã tới cuối phạm vi hiện tại -> phải nhảy
        if i == current_end:
            # nếu không thể mở rộng hơn nữa -> unreachable
            if furthest == current_end:
                return -1
            jumps += 1
            current_end = furthest
            # nếu phạm vi mới chạm tới hoặc vượt cuối mảng -> xong
            if current_end >= n - 1:
                break

    return jumps


arr = [1, 4, 3, 2, 6, 7]
# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [0, 10, 20]
# arr = [9, 10, 1, 2, 3, 9, 4, 0, 0, 0, 0, 0, 0, 0, 1]

# arr = [1, 2, 0, 0, 0]
# arr = [5, 2, 9, 3]
arr = [1, 0, 0, 0, 20609, 5316, 4587, 5844, 17520]
# print(minJumps_c2(arr))

hash_table = {1: "Thang 1", 2: "Thang 2"}

n = 2
print(hash_table.get(n))
