from typing import List


# 轮流检查 m 和 n
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mi, ni = 0, 0
        tmp_nums1 = nums1[:]
        index = 0
        while mi < m or ni < n:
            if mi == m:
                nums1[index] = nums2[ni]
                ni += 1
            elif ni == n:
                nums1[index] = tmp_nums1[mi]
                mi += 1
            elif tmp_nums1[mi] >= nums2[ni]:
                nums1[index] = nums2[ni]
                ni += 1
            else:
                nums1[index] = tmp_nums1[mi]
                mi += 1
            index += 1


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    solution.merge(nums1, m, nums2, n)
    print(nums1)
