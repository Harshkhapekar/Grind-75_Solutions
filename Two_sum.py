class Solution:
    def twoSum(self ,nums: List[int], target: int) -> List[int]:
        seen = {}
        for index , num  in enumerate(nums):
            second_num = target - num
            if second_num in seen:
                return [seen[second_num] , index]
            seen[num] = index
        return []
