
def multistage_graph(graph, stages):
    n = len(graph)

    cost = [float('inf')] * n
    path = [-1] * n

    cost[n - 1] = 0

    for i in range(n - 2, -1, -1):
        for j in range(n):
            if graph[i][j] != 0:
                if graph[i][j] + cost[j] < cost[i]:
                    cost[i] = graph[i][j] + cost[j]
                    path[i] = j

    print("Minimum Cost:", cost[0])

    print("Shortest Path:", end=" ")
    vertex = 0

    while vertex != -1:
        print(vertex + 1, end=" ")
        vertex = path[vertex]


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (0 means no edge):")
graph = [list(map(int, input().split())) for _ in range(n)]

stages = int(input("Enter number of stages: "))

multistage_graph(graph, stages)

