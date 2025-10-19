from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        queue = deque([s])
        smallest = s
        
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            if cur < smallest:
                smallest = cur

            # Operation 1: Add 'a' to all odd indices
            arr = list(cur)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            add_str = ''.join(arr)

            # Operation 2: Rotate right by 'b'
            rot_str = cur[-b:] + cur[:-b]

            # Add to queue if new
            if add_str not in visited:
                queue.append(add_str)
            if rot_str not in visited:
                queue.append(rot_str)

        return smallest
