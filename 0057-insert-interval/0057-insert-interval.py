class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Strategy: 3 steps - before, during(merge), after
        res = []
        i = 0
        n = len(intervals)
        
        new_start = newInterval[0]
        new_end = newInterval[1]

        # Add all intervals that come strictly BEFORE the new interval: 
        # end of current interval appears before new_interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals into one big, stretch the interval into a new_interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the final merged new_interval
        res.append(newInterval)

        # Add remaining intervals that come strictly AFTER newInterval
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res