class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        # the strat is to sort and then merge pairs of skill[0], skill[-1] together then multiply them 
        skill.sort()
        total_skill = 0
        lo = 0
        hi = len(skill) - 1
        temp_skill = skill[lo] + skill[hi] # a check to see if the combined skills are equal so we get equal 

        while lo <= hi:
            if skill[lo] + skill[hi] != temp_skill:
                return -1
            total_skill += (skill[lo] * skill[hi])
            lo += 1
            hi -= 1
        
        return total_skill