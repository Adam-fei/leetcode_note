from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        if n == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = n
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    print(solution.search(nums, target))
