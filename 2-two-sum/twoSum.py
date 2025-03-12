class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        else:
            ptr_counter = 0
            for i in range(len(nums)):
                ptr_counter += 1
                
                