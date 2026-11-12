
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])

    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False

    # Union by rank
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


def kruskal(vertices, edges):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = list(range(vertices))
    rank = [0] * vertices

    total_cost = 0
    mst_edges = 0

    print("Edges in Minimum Spanning Tree:")

    for u, v, weight in edges:

        # Check whether edge forms a cycle
        if union(parent, rank, u, v):

            print(u, "-", v, ":", weight)

            total_cost += weight
            mst_edges += 1

            if mst_edges == vertices - 1:
                break

    if mst_edges != vertices - 1:
        print("Graph is disconnected!")
        return

    print("\nMinimum Cost:", total_cost)


# Main program
vertices = 5

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

kruskal(vertices, edges)
