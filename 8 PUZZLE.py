from collections import deque

def solve_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = set()
    moves = [-3, 3, -1, 1]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution:")
            for step in path + [state]:
                for i in range(0, 9, 3):
                    print(step[i:i+3])
                print()
            return

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)

        for move in moves:
            new = zero + move

            if 0 <= new < 9:
                if abs(move) == 1 and zero // 3 != new // 3:
                    continue

                next_state = list(state)
                next_state[zero], next_state[new] = (
                    next_state[new], next_state[zero]
                )
                next_state = tuple(next_state)

                if next_state not in visited:
                    queue.append((next_state, path + [state]))

    print("No solution found")

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solve_puzzle(start, goal)
