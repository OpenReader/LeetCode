class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        in_degree = {}
        for i in range(numCourses):
            in_degree[i] = 0
        for e in prerequisites:
            G[e[1]].append(e[0])
            in_degree[e[0]] += 1
        
        ret = []
        noin = []
        for v in in_degree:
            if in_degree[v] == 0:
                noin.append(v)
        
        while noin:
            v = noin.pop()
            ret.append(v)
            for u in G[v]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    noin.append(u)
        
        return ret if len(ret) == numCourses else []