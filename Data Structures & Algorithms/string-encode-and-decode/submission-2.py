class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = str(len(string))
            result += length + "#" + string
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            new_string = s[j + 1:j + length + 1]
            result.append(new_string)
            i = j + 1 + length
        return result
        """
        for i in range(len(s)):
            if s[i] == "#":
                iter_range = int(s[i-1])
                new_string = s[i + 1:i+iter_range + 1]
                result.append(new_string)
        return result
        """