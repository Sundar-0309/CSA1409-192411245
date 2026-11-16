from collections import deque

def kahn(graph):
    nodes = set(graph) | {child for children in graph.values() for child in children}
    indegree = {node: 0 for node in nodes}
    for children in graph.values():
        for child in children: indegree[child] += 1
    ready = deque(sorted(node for node, degree in indegree.items() if degree == 0)); order = []
    while ready:
        node = ready.popleft(); order.append(node)
        for child in graph.get(node, []):
            indegree[child] -= 1
            if indegree[child] == 0: ready.append(child)
    if len(order) != len(nodes): raise ValueError('cycle detected in attribute dependency graph')
    return order
