def dfs_with_cycle(graph, start):
    visited = set()
    recursion_stack = set()
    exploration_order = []
    cycle = []

    def visit(node, path):
        nonlocal cycle

        visited.add(node)
        recursion_stack.add(node)
        exploration_order.append(node)
        path.append(node)

        for neighbor in graph.get(node, []):
            if cycle:
                return

            if neighbor not in visited:
                visit(neighbor, path)
            elif neighbor in recursion_stack:
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                return

        recursion_stack.remove(node)
        path.pop()

    visit(start, [])
    return exploration_order, cycle
