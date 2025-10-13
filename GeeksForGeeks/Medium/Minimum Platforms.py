def minPlatform_c1(arr, dep):  # AI làm
    arr.sort()
    dep.sort()
    n = len(arr)

    plat_needed = 1  # ít nhất 1 sân ga
    result = 1
    i = 1  # trỏ tàu đến tiếp theo
    j = 0  # trỏ tàu rời tiếp theo

    while i < n and j < n:
        # Nếu tàu đến trước khi tàu kia rời đi -> cần thêm platform
        if arr[i] <= dep[j]:
            print(arr[i], dep[j])
            plat_needed += 1
            i += 1
        else:
            # Một tàu đã rời đi -> giảm platform
            plat_needed -= 1
            j += 1

        result = max(result, plat_needed)

    return result


# Ý tưởng làm bài này:
"""
1. Sắp xếp các chuyến tàu cho đúng trình tự
2. Cần 1 biến lưu trữ cần bao nhiêu ga trong giờ cao điểm - tăng giảm liên tục trong suốt 1 ngày
3. Cần 2 biến lưu trữ tàu đến tiếp theo và tàu rời tiếp theo
4. Cần 1 biến lưu trữ tối đa ga cần phải đáp ứng trong giờ cao điểm
"""


def minPlatform_c2(arr, dep):  # Làm lại
    arr.sort()
    dep.sort()
    n = len(arr)

    plat_cap = 1  # platform capacity (số lượng ga tối thiểu)
    max_cap = 1  # maximun capacity (số lượng ga cần cho giờ cao điểm)

    i = 1  # trỏ đến tàu đến tiếp theo
    j = 0  # trỏ đến tàu rời tiếp thep

    while i < n and j < n:
        if (arr[i] <= dep[j]):
            plat_cap += 1
            i += 1
        else:
            plat_cap -= 1
            j += 1

        max_cap = max(max_cap, plat_cap)

    return max_cap


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

# arr = [900, 1235, 1100]
# dep = [1000, 1240, 1200]
# print(minPlatform_c1(arr, dep))
print(minPlatform_c2(arr, dep))
