"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = sorted(intervals,key=lambda x: x.start)
        
        for i in range(1,len(intervals)):
            cur = starts[i]
            prv = starts[i-1]
            print(cur.start,cur.end)
            print(prv.start,prv.end)
            if cur.start < prv.end: return False
        return True 