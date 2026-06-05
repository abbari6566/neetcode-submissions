class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result  = []
        idx = 0
        while idx < len(s):
            jdx = idx
            while s[jdx] != "#":
                jdx += 1
            length = int(s[idx:jdx])
            result.append(s[jdx + 1 : jdx + 1 + length])
            idx  = jdx + 1 + length
        return result