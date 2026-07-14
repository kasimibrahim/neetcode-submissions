class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # num -> index

        for i, num in enumerate(nums):
            complement = target - num

            if seen.get(complement, '') != '':
                return [seen[complement], i]

            seen[num] = i
        