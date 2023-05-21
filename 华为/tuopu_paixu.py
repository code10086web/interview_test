
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
def tuopu_paixu(graph):
    in_degree={}
    for node in graph:
        in_degree[node]=0
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor]+=1
    res=[]
    q=[]
    for node in graph:
        if in_degree[node]==0:
            q.append(node)

    while q:
        pop_node=q.pop()
        res.append(pop_node)
        for node in graph[pop_node]:
            in_degree[node]-=1
            if in_degree[node]==0:
                q.append(node)
    if len(res)==len(graph):
        print(res)
    else:
        print("该图有环")





tuopu_paixu(graph)
