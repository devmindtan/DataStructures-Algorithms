import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(list1, list2):
    head = ListNode(0)
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Nối phần còn lại
    current.next = list1 if list1 else list2

    return head.next


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(2)

    list2 = ListNode(4)
    list2.next = ListNode(6)
    list2.next.next = ListNode(3)
    print(solve(list1, list2))
