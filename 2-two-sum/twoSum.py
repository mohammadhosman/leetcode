class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        else:
            ptr_counter = 0
            for i in range(len(nums)):
                ptr_counter = i + 1
                curr_i = nums[i]
                while ptr_counter < len(nums):
                    if curr_i + nums[ptr_counter] == target:
                        return [i, ptr_counter]
                    ptr_counter += 1
                
                