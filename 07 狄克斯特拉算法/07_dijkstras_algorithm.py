# 存贮所有节点及其邻居节点
graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}   # 终点没有任何邻居

# 存贮所有开销（开销是指从起点到节点的距离）
infinity = float('inf')   # 无穷大的表示
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 存贮父节点
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 记录已经处理过的节点
processed = set()


# 找出最小开销节点
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs.keys():
        new_cost = costs[node]
        if new_cost < lowest_cost and (node not in processed):
            lowest_cost = new_cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)





