from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum_list = []
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            run_sum_list.append(sum)
        return run_sum_list
