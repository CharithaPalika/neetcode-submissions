class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sorted_nums = sorted(nums)
        popped_list = self.pop_repeated(sorted_nums)
        max = 0
        counts = 0
        for i in range(len(popped_list)-1):
            if popped_list[i+1] - popped_list[i] == 1:
                counts+=1
            else:
                counts = 0
            
            if counts > max:
                max = counts
        
        return max+1

    def pop_repeated(self, sorted_nums):
        idx = []
        for i in range(len(sorted_nums)-1):
            rep = False
            if sorted_nums[i] == sorted_nums[i+1]:
                idx.append(i)
        popped_list = [sorted_nums[i] for i in range(len(sorted_nums)) if i not in idx]
        
        return popped_list

            
