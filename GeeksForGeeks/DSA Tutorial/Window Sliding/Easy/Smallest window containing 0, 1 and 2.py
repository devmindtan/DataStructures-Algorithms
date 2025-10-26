def smallestSubstring(S):
    S = [int(num) for num in str(S)]
    # Initialize variables
    n, i, k, cnt, min_len = len(S), 0, 0, 0, float("inf")

    # Frequency array
    freq = [0] * 3

    while k < n:
        freq[int(S[k])] += 1
        if freq[int(S[k])] == 1:
            cnt += 1
        print(cnt)

        if cnt == 3:
            while freq[int(S[i])] > 1:
                freq[int(S[i])] -= 1
                i += 1
            min_len = min(min_len, k - i + 1)
            freq[int(S[i])] -= 1
            i += 1
            cnt -= 1
        k += 1

    return -1 if min_len == float("inf") else min_len


S = 10212

# S = 12121
# S = "01212"
# S = "012"
S = "022001"
print(smallestSubstring(S))
