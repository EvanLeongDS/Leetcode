class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for bracket in s:
            if bracket == "[":
                stack.append(bracket)
            if stack and bracket == "]":
                stack.pop()
        
        if not stack:
            return 0

        lonely = len(stack)
        return (lonely + 1) //2

        