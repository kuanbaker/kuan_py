from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_save = [0] * n
        res = []

        for i in nums:
            if res_save[i-1] == 0:
                res_save[i-1] = 1
            else:
                res.append(i)

        return res


sol = Solution()
test_case = [4, 3, 2, 7, 8, 2, 3, 1]
sol.findDuplicates(test_case)
