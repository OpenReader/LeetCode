class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build graph
        G = {}
        E = set()
        in_degree = {}
        L = len(words)
        
        def addEdge(w1, w2, asc):
            l1, l2 = len(w1), len(w2)
            if l1 > l2:
                return addEdge(w2, w1, False)
            i = 0
            while i < l1 and w1[i] == w2[i]:
                G[w1[i]] = []
                G[w2[i]] = []
                i += 1
            if i == l1 and not asc:
                return False
            if i < l1:
                if asc:
                    E.add((w1[i], w2[i]))
                else:
                    E.add((w2[i], w1[i]))
                G[w1[i]] = []
                G[w2[i]] = []
                i += 1
            while i < l2:
                if i < l1:
                    G[w1[i]] = []
                G[w2[i]] = []
                i += 1
            return True
        
        if L == 1:
            return words[0]
        for i in range(L-1):
            if not addEdge(words[i], words[i+1], True):
                return ''
        for e in E:
            G[e[0]].append(e[1])
            in_degree[e[1]] = in_degree.setdefault(e[1], 0) + 1
        
        # topologic sort
        ret = ''
        zero_in = []
        
        for v in G:
            if v not in in_degree:
                zero_in.append(v)
        
        while zero_in:
            v = zero_in.pop()
            ret += v
            for u in G[v]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    zero_in.append(u)
            G.pop(v)
        
        return '' if G else ret