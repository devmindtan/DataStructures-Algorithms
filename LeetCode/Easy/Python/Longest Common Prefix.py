from typing import List


def longestCommonPrefix(strs: List[str]):
    hash_table = {}
    res = [[] for _ in range(len(strs))]
    for ch in range(len(strs)):
        n = strs[ch]
        for i in range(len(n)):
            hash_table[ch[i]] = hash_table.get(ch[i], 0) + 1
            res[i].append(hash_table[ch[i]])
    # for num in strs:

    return res


strs = ["ddcogs"]
print(longestCommonPrefix(strs))
