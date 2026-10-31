class Solution:
    def robotWithString(self, s: str) -> str:
        # PART 1: for each index i, what's the smallest letter from i to the end?
        min_right = [''] * len(s)
        # TODO: fill it using the backwards loop you just fixed
        for i in range(len(s)-1, -1, -1):
            if i == len(s) - 1:
                min_right[i] = s[i]
            else:
                min_right[i] = min(s[i], min_right[i+1])
        print(min_right)

        # PART 2: walk through s
        t = []   # stack
        p = []
        for i in range(len(s)):
            t.append(s[i])

            # TODO: while t has stuff AND t[-1] <= smallest letter still left in s:
            while t and i+1 < len(s) and t[-1] <= min_right[i+1]:
            #           pop t into p
                popped = t.pop()
                p.append(popped)
        # TODO: anything still stuck in t?
        while t:
            popped = t.pop()
            p.append(popped)
        return "".join(p) 