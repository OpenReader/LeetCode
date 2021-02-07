class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score = 0
        h = [-a, -b, -c]
        heapify(h)
        fir, sec = -heappop(h), -heappop(h)
        while fir > 0 and sec > 0:
            if -h[0] == 0:
                get_score = sec
            else:
                get_score = sec + h[0] + 1
            score += get_score
            sec -= get_score
            fir -= get_score
            heappush(h, -fir)
            heappush(h, -sec)
            fir, sec = -heappop(h), -heappop(h)
        
        return score