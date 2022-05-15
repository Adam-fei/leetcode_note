class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in "[{(":
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                else:
                    last_item = stack.pop()
                    if (item == "]" and last_item == "[") or (item == "}" and last_item == "{") or (item == ")" and last_item == "("):
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    s = "{[]}"
    
    print(solution.isValid(s))
