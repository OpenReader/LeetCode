class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda v: v[0])
        # print(intervals)
        pre_end = -1
        for v in intervals:
            if v[0] >= pre_end:
                pre_end = v[1]
            else:
                return False
        return True