class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations)
        if L == 0 or citations[-1] == 0:
            return 0
        start, end = 0, L - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if citations[mid] >= L - mid:
                end = mid
            else:
                start = mid
        return L - start if citations[start] >= L - start else L - end