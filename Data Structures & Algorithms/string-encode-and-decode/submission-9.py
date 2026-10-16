class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ""
        for s in strs:
            ret_str += str(len(s)) + "#" + s
        return ret_str
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            str_len = ""
            word = ""
            while s[i] != "#":
                str_len += s[i]
                i+=1
            for j in range(i+1, i+int(str_len)+1):
                word += s[j]
            i += 1+len(word)
            ret.append(word)
        return ret
