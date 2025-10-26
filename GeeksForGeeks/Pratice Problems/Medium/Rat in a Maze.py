from collections import deque


def ratInMaze(maze):
    paths = bfs(maze)
    res = [path_to_directions(p) for p in paths]
    res.sort()
    return res


def bfs(matrix):
    rows, cols = len(matrix), len(matrix[0])
    start = (0, 0)
    end = (rows-1, cols-1)
    q = deque([(start, [start])])
    all_paths = []
    while q:
        (r, c), path = q.popleft()

        if (r, c) == end:
            all_paths.append(path)
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1 and (nr, nc) not in path):
                q.append(((nr, nc), path + [(nr, nc)]))

    return all_paths


def path_to_directions(path):
    directions = {(1, 0): "D", (-1, 0): "U", (0, 1): "R", (0, -1): "L"}
    visualize = ""
    for (r1, c1), (r2, c2) in zip(path, path[1:]):
        dr = r2 - r1
        dc = c2 - c1
        visualize += (directions[(dr, dc)])
    return visualize
