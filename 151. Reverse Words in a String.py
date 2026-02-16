class Solution:
    def reverseWords(self, s: str) -> str:
        return Solution._calc_res_method_1(s)
    
    @staticmethod
    def _calc_res_method_1(s: str):
        words = s.split()

        res = ""
        for idx in range(len(words)-1, -1, -1):
            if words[idx] != "":
                res += words[idx]
            if idx != 0:
                res += " "
        return res 
    