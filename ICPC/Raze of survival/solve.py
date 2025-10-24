from collections import deque
from itertools import combinations, permutations


def find_positions(grid, R, C):
    start = end = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "D":
                end = (r, c)
    return start, end


def bfs(grid, R, C):
    start, end = find_positions(grid, R, C)
    q = deque([(start[0], start[1], 3, 0)])
    seen = set([(start[0], start[1], 3)])
    res = -1

    while q:
        r, c, hp, d = q.popleft()
        if (r, c) == end and hp > 0:
            res = d
            break

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                nhp = hp - (grid[nr][nc] == "+")
                if nhp > 0 and (nr, nc, nhp) not in seen:
                    seen.add((nr, nc, nhp))
                    q.append((nr, nc, nhp, d + 1))

    return res


def solve():
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]

    print(bfs(grid, R, C))
