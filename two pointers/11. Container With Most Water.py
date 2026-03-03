class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(height)-1

        max_water_amount = float("-inf")
        while l_ptr < r_ptr:

            current_water_amount = (
                min( height[l_ptr], height[r_ptr] ) * ( r_ptr - l_ptr )
            )
            max_water_amount = max(
                current_water_amount, 
                max_water_amount
            )

            if height[l_ptr] <= height[r_ptr]:
                l_ptr += 1
            else:
                r_ptr -= 1
        
        return max_water_amount
        