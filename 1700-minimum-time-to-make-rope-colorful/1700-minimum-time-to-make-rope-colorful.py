class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        prev_max_time = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total_time += min(prev_max_time, neededTime[i])
                prev_max_time = max(prev_max_time, neededTime[i])
            else:
                prev_max_time = neededTime[i]
        
        return total_time
