class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # l=len(spells)
        # arr=[0]*l
        # for i in range (0,l):
        #     for j in range(0,(len(potions))):
        #         if (spells[i]*potions[j]>=success):
        #             arr[i]+=1
        # return arr

       
        potions.sort()
        m = len(potions)
        ans = []

        for s in spells:
            # Find minimum potion needed
            need = (success + s - 1) // s  # ceiling division

            # Binary search manually
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] < need:
                    l = mid + 1
                else:
                    r = mid - 1

            ans.append(m - l)
        return ans
