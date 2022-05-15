from typing import List


# 二分法
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 0 if nums[0] > nums[1] else 1
        start = 0
        mid = int(n/2)
        end = n
        while (start < mid) and (mid < end) and (0 < mid < n-1):
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                break
            elif nums[mid-1] > nums[mid]:
                end = mid
            else:
                start = mid
            mid = int((start + end) / 2)
        return mid


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 1]

    print(solution.findPeakElement(nums))
