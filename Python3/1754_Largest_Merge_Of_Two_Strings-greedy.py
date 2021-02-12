class Solution:
    # bfs with memo solution will meet time limit
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        s1, s2 = len(word1), len(word2)
        i, j = 0, 0
        while i < s1 and j < s2:
            if word1[i:] >= word2[j:]:
                merge += word1[i]
                i += 1
            else:
                merge += word2[j]
                j += 1
        return merge + word1[i:] + word2[j:]