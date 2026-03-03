class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_ptr = 1
        N = len(nums)

        for r_ptr in range(1, N):
            if nums[r_ptr] != nums[l_ptr - 1]:  # compare with last confirmed unique
                nums[l_ptr] = nums[r_ptr]
                l_ptr += 1

        return l_ptr

        return l_ptr

