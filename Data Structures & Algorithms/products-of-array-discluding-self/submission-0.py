class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in nums]
        carry = 1
        for index in range(len(nums)):
            output[index] *= carry
            carry *= nums[index]
        
        carry = 1
        for index in range(len(nums)-1, -1, -1):
            output[index] *= carry
            carry *= nums[index]
        return output
