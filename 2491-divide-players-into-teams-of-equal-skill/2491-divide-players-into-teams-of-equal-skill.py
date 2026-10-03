class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        lo = 0
        hi = len(skill) - 1

        skill_total = skill[0] + skill[-1] 
        pairs = [] # we will loop through this later 
        while lo <= hi:
            team_total = skill[lo] + skill[hi]
            if team_total != skill_total:
                return -1 
            else:
                pairs.append((skill[lo], skill[hi]))
            lo += 1
            hi -= 1
        
        total_skill = 0
        for player1, player2 in pairs:
            total_skill += player1 * player2
        
        return total_skill