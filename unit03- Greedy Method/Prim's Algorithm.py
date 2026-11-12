
def prim(graph, vertices):
    selected = [False] * vertices

    selected[0] = True

    total_cost = 0

    print("Edges in Minimum Spanning Tree:")

    for _ in range(vertices - 1):

        minimum = float('inf')
        x = -1
        y = -1

        # Find minimum edge connecting selected
        # and unselected vertices
        for i in range(vertices):

            if selected[i]:

                for j in range(vertices):

                    if not selected[j] and graph[i][j] != 0:

                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        # Select the minimum edge
        if y == -1:
            print("Graph is disconnected!")
            return

        print(x, "-", y, ":", minimum)

        total_cost += minimum
        selected[y] = True

    print("\nMinimum Cost:", total_cost)


# Main program
vertices = 5

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph, vertices)
