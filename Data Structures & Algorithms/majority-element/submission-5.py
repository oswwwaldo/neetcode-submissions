class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_dict: dict[int, int] = {}
        for unique_num in set(nums):
            nums_dict[unique_num] = nums.count(unique_num)
        return max(nums_dict.items(), key=lambda n: n[1])[0]