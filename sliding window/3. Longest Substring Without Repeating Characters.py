from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        N = len(s)
        window_elems = defaultdict(int)
        
        l_ptr = 0
        max_size = 0 
        
        for r_ptr in range(N):
            window_elems[ s[r_ptr] ] += 1

            while self.is_window_valid(window_elems) == False:
                window_elems[ s[l_ptr] ] -=1 
                if window_elems[ s[l_ptr] ] == 0:
                    del window_elems[ s[l_ptr] ]
                l_ptr += 1
            
            # print(window_elems)
        
            curr_size = len(window_elems)
            max_size = max( max_size, curr_size )

        return max_size

    def is_window_valid(self, window_elems):
        for key, value in window_elems.items():
            if value > 1:
                return False 
        return True