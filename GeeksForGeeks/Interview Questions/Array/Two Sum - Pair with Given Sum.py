def twoSum(arr, target):
    s = set()

    for num in arr:
        complement = target - num

        if (complement in s):
            return True

        s.add(num)

    return False


if __name__ == "__main__":
    target = int(input())
    arr = list(map(int, input().split()))
    print(twoSum(arr, target))
