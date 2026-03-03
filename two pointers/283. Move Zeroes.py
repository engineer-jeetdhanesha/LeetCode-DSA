class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read_ptr = 0
        write_ptr = 0 
        N = len(nums)

        for read_ptr in range(N):
            if nums[read_ptr] != 0:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
            
        while write_ptr < N:
            nums[write_ptr] = 0
            write_ptr += 1
        
            
            

        