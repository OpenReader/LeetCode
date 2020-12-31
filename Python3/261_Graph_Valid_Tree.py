class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        G = defaultdict(lambda: [])
        for e in edges:
            G[e[0]].append(e[1])
            G[e[1]].append(e[0])
        
        visited = set([0])
        sk = [0]
        while sk:
            cur = sk.pop()
            for ad in G[cur]:
                if ad not in visited:
                    sk.append(ad)
                    visited.add(ad)
        return True if len(visited) == n else False