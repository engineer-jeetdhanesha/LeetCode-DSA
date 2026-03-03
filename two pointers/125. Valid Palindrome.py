class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_ptr = 0
        r_ptr = len(s)-1


        while l_ptr < r_ptr:
            p = s[l_ptr].lower()
            ascii_p = ord(p) 
            if not p.isalnum():
                l_ptr += 1 
                continue
            
            q = s[r_ptr].lower()
            ascii_q = ord(q) 
            if not q.isalnum():
                r_ptr -= 1 
                continue
                
            if p != q:
                
                return False
            
            l_ptr += 1
            r_ptr -= 1
        
        return True
            
