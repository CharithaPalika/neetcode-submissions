class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        KFrequent = {}
        idx = []
        for i in range(len(nums)):
            if i in idx:
                continue
            counts = 1
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counts += 1
                    idx.append(j)
            KFrequent[nums[i]] = counts
        counts_sorted = sorted(KFrequent.values(), reverse = True)

        k = [key for key, value in KFrequent.items() if value in counts_sorted[0:k]]
        return k
