class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        curr = 0
        boxes = 0
        for cap in capacity:
            curr += cap
            boxes += 1
            if curr >= total_apples:
                return boxes
