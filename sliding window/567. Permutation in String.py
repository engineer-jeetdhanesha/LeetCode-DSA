from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq = defaultdict(int)

        for elem in s1:
            s1_freq[elem] +=1 
        

        N_s1 = len(s1)
        N_s2 = len(s2)

        s2_freq = defaultdict(int)

        for i in range(N_s2):
            s2_freq[ s2[i] ] += 1

            if i >= N_s1:
                s2_freq[ s2[i-N_s1] ] -= 1
                if s2_freq[ s2[i-N_s1] ] == 0:
                    del s2_freq[ s2[i-N_s1] ]
            
            if i >= N_s1 - 1:
                # print(s1_freq, s2_freq)
                if s2_freq == s1_freq:
                    return True
            
        return False
        