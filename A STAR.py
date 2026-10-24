def astar(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    parent = {}
    g_cost = {start: 0}

    while open_list:
        open_list.sort(key=lambda x: x[1])
        node, f = open_list.pop(0)

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            print("Path:", path[::-1])
            print("Cost:", g_cost[goal])
            return

        for neighbor, cost in graph[node].items():
            new_cost = g_cost[node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = node
                f_cost = new_cost + heuristic[neighbor]
                open_list.append((neighbor, f_cost))

    print("No path found")

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 3},
    'E': {'G': 2},
    'G': {}
}

heuristic = {
    'A': 6, 'B': 5, 'C': 3,
    'D': 3, 'E': 1, 'G': 0
}

astar(graph, heuristic, 'A', 'G')
