from typing import List


# 分别找到正确的左右边界
class Solution:
    def getLeftBorder(self, nums, target):
        left = 0
        right = len(nums) - 1
        leftBoder = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        leftBoder = left if nums[left] == target else -1
        return leftBoder

    def getRightBorder(self, nums, target):
        left = 0
        right = len(nums) - 1
        rightBorder = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        rightBorder = right if nums[right] == target else -1
        return rightBorder

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        n = len(nums)
        if n == 0:
            return result
        if n == 1:
            if nums[0] == target:
                result = [0, 0]
            return result

        if target < nums[0] or target > nums[-1]:
            return result


        # find left border index
        LeftBorder = self.getLeftBorder(nums, target)
        rightBoder = self.getRightBorder(nums, target)

        return [LeftBorder, rightBoder]


if __name__ == "__main__":
    solution = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    print(solution.searchRange(nums, target))
