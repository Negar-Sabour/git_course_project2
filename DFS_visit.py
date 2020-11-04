def DFS_visit(node,colorsDic,colors,pre,G):
    #function defenition
    #new line
    colors[node] = colorsDic["gray"]
    for adjNode in G[node]:
        if colors[adjNode] == colorsDic["white"]:
            pre [adjNode] = node
            (a,b) = DFS_visit(adjNode,colorsDic,colors,pre,G)
        if (a,b) != (-1,-1):
                return (a,b)
        elif colors[adjNode] == colorsDic["gray"]:
            return (node,adjNode)

    colors[node] = colorsDic["black"]
    return (-1,-1)
