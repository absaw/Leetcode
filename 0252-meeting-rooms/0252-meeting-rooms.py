class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key = lambda i:i[0])
        print(intervals)
        for i in range(1,len(intervals)):

            if intervals[i][0] < intervals[i-1][1]:
                return False
            
        return True