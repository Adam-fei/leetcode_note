# 动态规划, 以正方形右下角为突破口
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        max_s = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_s = max(max_s, dp[i][j])
        
        max_square = max_s*max_s
        return max_square


if __name__ == "__main__":
    solution = Solution()

    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    print(solution.maximalSquare(matrix))
