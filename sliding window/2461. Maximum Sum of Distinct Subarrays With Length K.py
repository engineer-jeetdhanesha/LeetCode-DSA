from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        window_elems = defaultdict(int)

        max_sum = 0
        current_sum = 0

        for i in range(N):

            window_elems[ nums[i] ] += 1
            current_sum += nums[i]

            if i >= k:
                window_elems[ nums[i-k] ] -= 1
                current_sum -= nums[i-k]
                if window_elems[ nums[i-k] ] <= 0:
                    del window_elems[ nums[i-k] ]
            
            if i >= k-1:
                if len(window_elems) == k:
                    max_sum = max( current_sum, max_sum )

        return max_sum