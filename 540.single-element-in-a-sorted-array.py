from typing import List


# 寻找不寻常元素的 index 是奇数还是偶数
class Solution:
    def isEven(self, num):
        if num%2 == 0:
            return True
        else:
            return False
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        start = 0
        end = len(nums)-1
        mid = int((start+end)/2)
        while start < mid < end:
            if nums[mid] == nums[mid-1]:
                if self.isEven(mid):
                    end = mid
                else:
                    start = mid+1
                mid = int((start+end)/2)
            elif nums[mid] == nums[mid+1]:
                if self.isEven(mid):
                    start = mid
                else:
                    end = mid-1
                mid = int((start+end)/2)
            else:
                return nums[mid]
        return nums[mid]


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

    print(solution.singleNonDuplicate(nums))
