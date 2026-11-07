
roads = [
    ("Arad", "Zerind", 75), ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71), ("Oradea", "Sibiu", 151),
    ("Timisoara", "Lugoj", 111), ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75), ("Dobreta", "Craiova", 120),
    ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Craiova", 146), ("Rimnicu Vilcea", "Pitesti", 97),
    ("Craiova", "Pitesti", 138), ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101), ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85), ("Urziceni", "Hirsova", 98),
    ("Urziceni", "Vaslui", 142), ("Hirsova", "Eforie", 86),
    ("Vaslui", "Iasi", 92), ("Iasi", "Neamt", 87),
]

h = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Eforie": 161,
    "Fagaras": 178, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 98,
    "Rimnicu Vilcea": 193, "Sibiu": 253, "Timisoara": 329, "Urziceni": 80,
    "Vaslui": 199, "Zerind": 374,
}

graph = {}

for city1, city2, dist in roads:
    graph.setdefault(city1, {})[city2] = dist
    graph.setdefault(city2, {})[city1] = dist


def search(start, goal, h, use_g):

    frontier = [(start, 0, [start])]
    explored = []
    best_g = {start: 0}
    expanded = 0
    max_frontier = 1

    while len(frontier) > 0:
        best = frontier[0]

        for item in frontier:
            city, g, path = item
            f = h[city] + (g if use_g else 0)

            best_city, best_cost, best_path = best
            best_f = h[best_city] + (best_cost if use_g else 0)

            if f < best_f:
                best = item

        frontier.remove(best)
        city, g, path = best

        if city in explored:
            continue

        if city == goal:
            return path, g, expanded, max_frontier

        explored.append(city)
        expanded += 1

        for next_city, dist in graph[city].items():
            new_g = g + dist

            if next_city in explored:
                continue

            if use_g and new_g >= best_g.get(next_city, 10**9):
                continue

            if not use_g and next_city in best_g:
                continue

            best_g[next_city] = new_g
            frontier.append((next_city, new_g, path + [next_city]))

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

    return None, 0, expanded, max_frontier


def greedy(start, goal, h):
    return search(start, goal, h, False)


def astar(start, goal, h):
    return search(start, goal, h, True)


def show(start, name, result):
    path, cost, expanded, max_frontier = result

    print(start, "|", name, "| cost =", cost, "| expanded =", expanded,
          "| max frontier =", max_frontier)

    print("  path:", " -> ".join(path))


goal = "Bucharest"
h_zero = {}
h_double = {}

for city in h:
    h_zero[city] = 0
    h_double[city] = 2 * h[city]


print("=== Main comparison table ===")

for start in ["Arad", "Timisoara"]:
    show(start, "Greedy BFS", greedy(start, goal, h))
    show(start, "A*", astar(start, goal, h))

show("Arad", "A* (h = 0)", astar("Arad", goal, h_zero))
show("Arad", "A* (2 x h)", astar("Arad", goal, h_double))


print("\n=== Optional: A* with h = 0 and 2 x h from Timisoara ===")

show("Timisoara", "A* (h = 0)", astar("Timisoara", goal, h_zero))
show("Timisoara", "A* (2 x h)", astar("Timisoara", goal, h_double))


print("\n=== Optional: Greedy BFS with h = 0 and 2 x h ===")

for start in ["Arad", "Timisoara"]:
    show("Arad" if start == "Arad" else "Timisoara",
         "Greedy (h = 0)", greedy(start, goal, h_zero))

    show(start, "Greedy (2 x h)", greedy(start, goal, h_double))


print("\n=== Admissibility check: h(n) vs real shortest distance ===")
print("City | h(n) | real distance | h(n) <= real?")

for city in ["Arad", "Timisoara", "Sibiu", "Rimnicu Vilcea", "Pitesti",
             "Fagaras", "Craiova", "Lugoj"]:

    real = astar(city, goal, h_zero)[1]

    print(city, "|", h[city], "|", real, "|", h[city] <= real)
