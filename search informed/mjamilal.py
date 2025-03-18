import heapq

graph = {
    'S': [('A', 2), ('B', 3)],
    'A': [('D', 9), ('B', 2)],
    'B': [('C', 7)],
    'C': [('D', 0), ('G', 5)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 3,
    'A': 4,
    'B': 9,
    'C': 3,
    'D': 0,
    'G': 1,
}

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, []))

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        path = path + [current]

        if current == goal:
            return path, g

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path))

    return None, float('inf')

start_node = 'S'
goal_node = 'G'
path, cost = a_star_search(start_node, goal_node)

if path:
    print("Path ditemukan:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("Tidak ada jalur yang ditemukan")
