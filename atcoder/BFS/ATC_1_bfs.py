import sys

h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for j in range(h)]
queue =[]

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            queue.append([i,j])
            visited[i][j] = 1


dy_dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while len(queue) > 0:
    now = queue.pop(0)
    if c[now[0]][now[1]] == "g":
        print("Yes")
        sys.exit()
    for i in range(4):
        y = now[0] + dy_dx[i][0]
        x = now[1] + dy_dx[i][1]
        if 0 <= y < h and 0 <= x < w:
            if c[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = 1
                queue.append([y, x])

print("No")
