from bisect import bisect_left

class Solution:
    def maxTwoEvents(self, events):
        # Sort by start time
        events.sort(key=lambda x: x[0])
        n = len(events)

        # Build suffix max of values
        suffixMax = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], events[i][2])

        # Extract start times for binary search
        starts = [e[0] for e in events]

        ans = 0
        for i in range(n):
            start, end, val = events[i]
            # Find first event starting at or after end + 1
            j = bisect_left(starts, end + 1)
            ans = max(ans, val + suffixMax[j])

        return ans
