class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l_ptr = 0 
        r_ptr = len(numbers) - 1

        N = len(numbers)

        while l_ptr < r_ptr:
            
            current_sum = numbers[l_ptr] + numbers[r_ptr]

            if current_sum == target:
                return [l_ptr+1, r_ptr+1]
            
            elif current_sum < target:
                l_ptr += 1
            
            else:
                r_ptr-= 1
        
        return []