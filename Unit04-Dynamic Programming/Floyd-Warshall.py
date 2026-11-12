
def floyd_warshall(graph):
    n = len(graph)

    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    print("Shortest Distance Matrix:")

    for row in dist:
        print(row)


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (-1 for no edge):")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == -1:
            row[j] = float('inf')
    graph.append(row)

floyd_warshall(graph)
