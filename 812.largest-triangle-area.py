from typing import List


# 向量法
class Solution:
    def getAera(self, points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        return ((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3)) / 2

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_aera = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    aera = self.getAera([points[i], points[j], points[k]])
                    aera = abs(aera)
                    if aera > max_aera:
                        max_aera = aera

        return max_aera


if __name__ == "__main__":
    solution = Solution()

    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]

    print(solution.largestTriangleArea(points))
