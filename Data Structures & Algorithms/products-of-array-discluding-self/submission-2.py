class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[j] == 0:
                    pdt = 0
                    break
                else:
                    pdt *= nums[j]
            output.append(pdt)
        return output
            
        