from typing import List, Optional, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        table: Dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in table:
                return [table[num], i]
            table[target - num] = i
        return None
