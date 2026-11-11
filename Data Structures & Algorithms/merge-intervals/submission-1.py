class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1) combine the intervals that have the same start time/different end time ([1,2][1,5])->[1,5]) and same end time/different start time ([2,6],[4,6]->[2,6])
        2) check for overlap with consecutuve have the same end as the next's start

        """
        intervals.sort()
        output=[intervals[0]]

        for start,end in intervals:
            lastEnd=output[-1][1]

            if start<=lastEnd:
                #merge
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])
        return output
            
            