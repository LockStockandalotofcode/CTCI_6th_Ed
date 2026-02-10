class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the input list in-place by the first index
        intervals.sort(key=lambda x: x[0])

        res = []
        
        for interval in intervals:
            # if res is empty or there's no overlap with the last merged
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # if there's an overlap, merge the current interval with the last one in 'res' by updating the end time
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res