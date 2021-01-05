class Solution:
    
    # Counting: O(n)
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations)
        cnt = [0] * (L+1)
        for n in citations:
            if n >= L:
                cnt[L] += 1
            else:
                cnt[n] += 1
        acc = 0
        for i in range(L, -1, -1):
            acc += cnt[i]
            if acc >= i:
                return i
        return 0
    
    # # sort solution cost O(nlog)
    # def hIndex(self, citations: List[int]) -> int:
    #     citations.sort(reverse=True)
    #     for i, n in enumerate(citations):
    #         if n < i + 1:
    #             return i
    #     return len(citations)