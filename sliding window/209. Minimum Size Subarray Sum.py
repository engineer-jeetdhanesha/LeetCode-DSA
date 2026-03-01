class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        N = len(nums)

        l_ptr = 0 
        r_ptr = 0
        current_sum = 0
        min_size = float("inf") 

        while r_ptr < N:
            current_sum += nums[r_ptr]
            
            while current_sum >= target and l_ptr <= r_ptr:

                min_size = min(min_size, r_ptr - l_ptr + 1)
                current_sum -= nums[l_ptr] 

                l_ptr += 1
            
            r_ptr += 1
        
        return 0 if min_size == float("inf") else min_size 