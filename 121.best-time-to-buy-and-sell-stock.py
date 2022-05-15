from typing import List


# 只循环一次
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        if n == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0

        min_value = prices[0]
        max_profit = 0

        for i in range(1, n):
            temp = prices[i] - min_value
            if temp >= max_profit:
                max_profit = temp
            if prices[i] <= min_value:
                min_value = prices[i]
        
        return max_profit


if __name__ == "__main__":
    solution = Solution()

    prices = [7,1,5,3,6,4]

    print(solution.maxProfit(prices))
