class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        intervals.sort()#first sorts by start val then the end val
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                counter += 1
                prevEnd = min(prevEnd, end)

        return counter
#Time - O(NlogN) due to sort
        