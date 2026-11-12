
def tsp_branch_bound(graph):
    n = len(graph)

    if n == 1:
        print("Minimum Cost:", 0)
        print("Optimal Path: 1 -> 1")
        return

    best_cost = float('inf')
    best_path = []

    def calculate_bound(path, visited, current_cost):
        unvisited = [i for i in range(n) if not visited[i]]

        if not unvisited:
            return current_cost + graph[path[-1]][0]

        # Minimum outgoing edge from current city
        current_edges = [
            graph[path[-1]][v] for v in unvisited
        ]

        if not current_edges:
            return float('inf')

        lower_bound = current_cost + min(current_edges)

        # Minimum outgoing edge for every unvisited city
        for u in unvisited:
            possible_edges = [
                graph[u][v]
                for v in range(n)
                if v != u and (not visited[v] or v == 0)
            ]

            if not possible_edges:
                return float('inf')

            lower_bound += min(possible_edges)

        return lower_bound

    def backtrack(path, visited, current_cost):
        nonlocal best_cost, best_path

        current_city = path[-1]

        # All cities visited: return to starting city
        if len(path) == n:
            total_cost = current_cost + graph[current_city][0]

            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path.copy() + [0]

            return

        # Try all unvisited cities
        for next_city in range(1, n):
            if not visited[next_city]:

                new_cost = current_cost + graph[current_city][next_city]

                if new_cost >= best_cost:
                    continue

                visited[next_city] = True
                path.append(next_city)

                bound = calculate_bound(
                    path, visited, new_cost
                )

                if bound < best_cost:
                    backtrack(path, visited, new_cost)

                path.pop()
                visited[next_city] = False

    visited = [False] * n
    visited[0] = True

    backtrack([0], visited, 0)

    if best_path:
        print("Minimum Cost:", best_cost)
        print("Optimal Path:", " -> ".join(
            str(city + 1) for city in best_path
        ))
    else:
        print("No valid tour exists")


n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

if n <= 0 or any(len(row) != n for row in graph):
    print("Invalid cost matrix")
else:
    tsp_branch_bound(graph)
