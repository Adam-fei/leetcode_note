from typing import List


# 3sum 外面包了一层循环
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        length = len(nums)
        if length < 4:
            return ans
        elif length == 4:
            return [nums,] if sum(nums) == target else []
        nums.sort()
        for idx in range(length-3):
            if sum(nums[idx:idx + 4]) > target:
                break
            if nums[idx] + sum(nums[length-3:]) < target:
                continue
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            anchor = target - nums[idx]

            for i in range(idx+1, length-2):
                if nums[idx] + sum(nums[i:i + 3]) > target:
                    break
                if nums[idx] + nums[i] + sum(nums[length - 2:]) < target:
                    continue
                if i > idx+1 and nums[i] == nums[i-1]:
                    continue

                anchor_2 = anchor - nums[i]
                j = i + 1
                k = length-1
                while j < k:
                    if j > i+1 and nums[j] == nums[j-1]:
                        j += 1
                        continue
                    if k < length-1 and nums[k] == nums[k+1]:
                        k -= 1
                        continue
                    if nums[j] + nums[k] == anchor_2:
                        ans.append([nums[idx], nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] > anchor_2:
                        k -= 1
                    else:
                        j += 1
        return ans


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    print(solution.fourSum(nums, target))
