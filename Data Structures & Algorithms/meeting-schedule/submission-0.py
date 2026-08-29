"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#missed 1 detail, Interval is just not an iterable object like list, tuples
#it is a class defined above
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        prevEnd = intervals[0].end

        for interval in intervals[1:]:
            if prevEnd > interval.start:
                return False #conflict found
            else:
                prevEnd = interval.end
        #if it ends loop means no conflict
        return True
#due to sort, time becomes O(n log n)