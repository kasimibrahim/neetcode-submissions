class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for each_num in nums:
            duplicates[each_num] = duplicates.get(each_num, 0) + 1
            if duplicates[each_num] > 1:
                return True
        return False
        