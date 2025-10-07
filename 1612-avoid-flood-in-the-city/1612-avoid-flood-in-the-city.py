class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n
        full = {}         # lake -> last filled day
        dry_days = []     # indices of days we can dry lakes

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
            else:
                if lake in full:
                    # We need to dry this lake before today
                    found = False
                    for j in range(len(dry_days)):
                        if dry_days[j] > full[lake]:
                            dry_day = dry_days[j]
                            ans[dry_day] = lake  # use that dry day
                            dry_days.pop(j)
                            found = True
                            break
                    if not found:
                        return []  # no suitable dry day -> flood
                full[lake] = i
                ans[i] = -1  # raining day

        # Remaining dry days can dry any lake (say lake 1)
        for d in dry_days:
            ans[d] = 1

        return ans
