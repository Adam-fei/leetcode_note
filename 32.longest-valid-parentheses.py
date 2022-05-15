# 重点在于栈中储存的是暂未配对成功的括号的 index
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

            top_value = stack[-1] if stack else -1
            max_len = max(max_len, i - top_value)
        return max_len


if __name__ == "__main__":
    solution = Solution()

    s = ")()())"

    print(solution.longestValidParentheses(s))
