class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getDistance(c1, c2):
            return str((26 + ord(c2) - ord(c1)) % 26)
        
        distances = {}
        
        for s in strings:
            L = len(s)
            dis = ''
            for i in range(L):
                dis += getDistance(s[i], s[(i+L-1) % L]) + ' '
            if dis not in distances:
                distances[dis] = [s]
            else:
                distances[dis].append(s)
        
        # print(distances)
        ret = []
        for k in distances:
            ret.append(distances[k])
        
        return ret