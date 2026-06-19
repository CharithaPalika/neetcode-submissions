class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_anagrams = []
        idx = []
        for i in range(len(strs)):
            temp = []
            temp.append(strs[i])
            if i in idx:
                continue
            for j in range(i+1, len(strs)):
                if self.check_anagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    idx.append(j)
            final_anagrams.append(temp)
        
        return final_anagrams
                    
    def check_anagram(self, str_1, str_2):
        return sorted(str_1) == sorted(str_2)