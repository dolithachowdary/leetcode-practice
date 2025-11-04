import collections
from sortedcontainers import SortedList   # Requires installation of sortedcontainers

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        cnt = collections.Counter()
        # Each element in the sets is (frequency, value)
        top = SortedList()
        bot = SortedList()
        current_sum = 0
        n = len(nums)
        ans = []
        
        def _remove(val):
            nonlocal current_sum
            f = cnt[val]
            if f == 0:
                return
            key = (f, val)
            # Remove from whichever set it belongs
            if key in top:
                top.remove(key)
                current_sum -= f * val
            else:
                bot.remove(key)
        
        def _add(val):
            nonlocal current_sum
            f = cnt[val]
            if f == 0:
                return
            key = (f, val)
            # decide if it goes to top or bot
            if len(top) < x:
                top.add(key)
                current_sum += f * val
            else:
                # compare with smallest in top; if key is "better", swap
                if top and key > top[0]:
                    # move smallest top to bot
                    smallest_top = top.pop(0)
                    current_sum -= smallest_top[0] * smallest_top[1]
                    bot.add(smallest_top)
                    # put new key in top
                    top.add(key)
                    current_sum += f * val
                else:
                    bot.add(key)
        
        for i, v in enumerate(nums):
            # 1) prepare to add v
            _remove(v)
            cnt[v] += 1
            _add(v)
            
            # window start index
            if i >= k:
                old = nums[i - k]
                _remove(old)
                cnt[old] -= 1
                _add(old)
            
            if i >= k - 1:
                # ensure top has exactly x (or fewer if distinct < x)
                while len(top) < x and bot:
                    key = bot.pop()   # largest in bot
                    top.add(key)
                    current_sum += key[0] * key[1]
                # ensure no element in bot is "better" than any in top
                while bot and top and bot[-1] > top[0]:
                    keyB = bot.pop()
                    keyT = top.pop(0)
                    current_sum -= keyT[0] * keyT[1]
                    current_sum += keyB[0] * keyB[1]
                    bot.add(keyT)
                    top.add(keyB)
                
                ans.append(current_sum)
        
        return ans
