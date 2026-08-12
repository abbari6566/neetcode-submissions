class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start values
        #iterate  through start values
        #does current interval overalp with previous interval
        intervals.sort()
        output = [intervals[0]] #put for first interval
        '''
        for example [[1,3],[1,5],[6,7],[2,4]]
        after sorting should be [[1,3],[1,5],[2,4],[6,7]]
        output = [[1,3]]
        '''
        for start, end in intervals[1:]: #start from 2nd lsit
            prevEnd = output[-1][1] #if start=1 end=5, then prevEnd=3
            if start <= prevEnd:
                output[-1][1] = max(end, prevEnd)
            else:
                #just merge no overalapping interval
                output.append([start,end])
        return output


        