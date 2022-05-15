from typing import List


# 二分法, 无重复, 升序
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            elif nums[0] < target:
                return 1
            else:
                return 0
        if nums[n-1] < target:
            return n
        start = 0
        end = n - 1
        mid = (start+end)//2

        while start < end:
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
            mid = int((start+end)/2)
        return mid


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 3, 5, 6]
    target = 5

    print(solution.searchInsert(nums, target))
