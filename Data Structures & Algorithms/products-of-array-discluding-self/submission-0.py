class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                pdt *= nums[j]
            output.append(pdt)
        return output
            
        