# class Node:
#     def __init__(self, data: int):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def search(self, data: int):
#         cur = self.head
#         while cur is not None:
#             if (cur.data == data):
#                 return True
#             cur = cur.next
#         return False

#     def traverse(self):
#         cur = self.head
#         while cur is not None:
#             print(cur.data, end=" -> ")
#             cur = cur.next
#         return None

#     def insertAtHead(self, data: int):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insertAtTail(self, data: int):
#         new_node = Node(data)
#         if (new_node is None):
#             self.head = new_node
#             return self.head
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = new_node

#     def insertAtPosition(self, idx: int, data: int):
#         if (idx == 0):
#             self.insertAtHead(data)
#             return

#         new_node = Node(data)
#         cur = self.head
#         count = 0
#         while cur is not None and count < idx-1:
#             cur = cur.next
#             count += 1

#         if (cur is None):
#             return "Run out of list"

#         new_node.next = cur.next
#         cur.next = new_node


# ll = LinkedList()

# ll.insertAtHead(10)
# ll.insertAtHead(11)
# ll.insertAtHead(12)
# ll.insertAtTail(13)
# ll.insertAtPosition(2, 4)
# # insertAtTail(head, 9)
# # print(search(head, 3))

# print(ll.traverse())

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, start):
    visited = set()           # Để đánh dấu node đã thăm
    queue = deque([start])    # Khởi tạo deque với node bắt đầu

    while queue:
        node = queue.popleft()   # Lấy node đầu tiên ra
        if node not in visited:
            print(node)         # Xử lý node (vd: in ra)
            visited.add(node)
            # Thêm các node lân cận chưa thăm vào cuối deque
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# bfs(graph, 'A')


grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

grid = [
    ["S", "+", "+", "D"],
    ["-", "-", "-", "-",],
]
start = (0, 0)
end = (0, 3)


def bfs(grid, start, end):
    q = deque([(start, [start])])
    all_paths = []
    while q:
        (r, c), path = q.popleft()

        if (r, c) == end:
            all_paths.append(path)
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in path:
                q.append(((nr, nc), path + [(nr, nc)]))

    return all_paths


def bfs_1(grid, start, end):
    hp = 3
    all_paths = []
    q = deque([(start, [start])])
    vis = set()

    while q:
        (x, y), path = q.popleft()
        if ((x, y) not in vis):
            vis.add((x, y))

            if ((x, y) == end):
                all_paths.append(path)
                continue

            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + r, y + c
                if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in vis):
                    q.append(((nx, ny), path + [(nx, ny)]))

    return all_paths


# def bfs_2(grid, start, end):
#     q = deque([(start, [start])])
#     vis = set()

#     while q:
#         (x, y), path = q.popleft()
#         if (x, y) not in vis:
#             vis.add((x, y))
#             if (x, y) == end:
#                 return path

#             for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 nx, ny = x + r, y + c
#                 if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in vis):
#                     q.append(((nx, ny), path + [(nx, ny)]))

#     return -1

# grid = [
#     ["S", "+", "+", "D"],
#     ["-", "-", "-", "-",],
# ]

# grid = [
#     ["S", "+", "+", "+", "D"],
#     ["+", "-", "+", "-", "-",],
# ]


def bfs(grid, R, C):
    start = (0, 0)
    end = (0, C-1)
    q = deque([(start, [start])])
    all_paths = []
    while q:
        (r, c), path = q.popleft()

        if (r, c) == end:
            all_paths.append(path)
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in path:
                q.append(((nr, nc), path + [(nr, nc)]))

    return all_paths


def solve():
    R, C = map(int, input().split())

    grid = []
    for i in range(R):
        column = input()
        grid.append(list(column))

    all_paths = bfs(grid, R, C)

    best_ways = {}

    for i in range(len(all_paths)):
        hp = 3
        for j in range(len(all_paths[i])):
            r, c = all_paths[i][j]
            if grid[r][c] == "+":
                hp -= 1

        steps = len(all_paths[i]) - 1

        if hp > 0:
            if hp not in best_ways:
                best_ways[hp] = []
            best_ways[hp].append(steps)

    valid_hp = [hp for hp in best_ways if hp > 0]

    if not valid_hp:
        print(-1)
        return

    best_len = min(min(best_ways[hp]) for hp in valid_hp)
    print(best_len)


# solve()
x1 = 1
y1 = 1
x2 = 5
y2 = 5

print((abs(x1-x2) + abs(y1-y2)))
