class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        N = len(s)

        l_ptr = 0
        r_ptr = N-1 

        while l_ptr < r_ptr:
            temp_chr = s[l_ptr]
            s[l_ptr] = s[r_ptr]
            s[r_ptr] = temp_chr

            l_ptr += 1
            r_ptr -= 1
        
        