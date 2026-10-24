from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        for a, b in moves:
            if boat == 1:
                nm, nc = m - a, c - b
                nb = 0
            else:
                nm, nc = m + a, c + b
                nb = 1

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            rm, rc = 3 - nm, 3 - nc

            if (nm == 0 or nm >= nc) and (rm == 0 or rm >= rc):
                new_state = (nm, nc, nb)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

solve()
