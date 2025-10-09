class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n = len(skill)
        m = len(mana)
        sumSkill = sum(skill)
        # finish time for potion 0 (after it has passed all wizards)
        prevWizardDone = sumSkill * mana[0]
        
        for j in range(1, m):
            prevPotionDone = prevWizardDone
            # go backwards through wizards except last
            for i in range(n - 2, -1, -1):
                # subtract time wizard i+1 had on potion j−1
                prevPotionDone -= skill[i + 1] * mana[j - 1]
                # ensure wizard i on potion j starts so that no conflict
                # i.e. can't start earlier than constraint from previous pipeline
                prevWizardDone = max(prevPotionDone,
                                     prevWizardDone - skill[i] * mana[j])
            # push the j-th potion through all wizards
            prevWizardDone += sumSkill * mana[j]
        
        return prevWizardDone
