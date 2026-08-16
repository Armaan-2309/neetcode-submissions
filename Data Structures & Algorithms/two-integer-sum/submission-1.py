class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i,num in enumerate(nums):
            x = target - num

            if x in map:
                return [map[x],i]

            map[num] = i