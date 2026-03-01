class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        N = len(nums)
        max_avg = float("-inf")
        current_sum = 0

        for i in range(N):
            current_sum += nums[i]

            if i >= k: 
                current_sum -= nums[i-k] 
            
            if i >= k-1:
                max_avg = max( max_avg, current_sum / k )
        
        return max_avg