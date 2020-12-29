class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        min_h = []
        num = 0
        for i in intervals:
            if not min_h:
                num = max(num, 1)
                heappush(min_h, i[1])
            else:
                if min_h[0] <= i[0]:
                    heappop(min_h)
                heappush(min_h, i[1])
                num = max(num, len(min_h))
        return num