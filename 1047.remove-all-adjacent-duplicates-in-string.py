# 栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack_list = []
        for item in s:
            if stack_list and item == stack_list[-1]:
                stack_list.pop()
            else:
                stack_list.append(item)
        
        return "".join(stack_list)


if __name__ == "__main__":
    solution = Solution()

    s = "abbaca"

    print(solution.removeDuplicates(s))
