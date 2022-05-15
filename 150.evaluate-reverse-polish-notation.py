# 栈
class Solution(object):
    def evalRPN(self, tokens):
        tmp_list = []
        for item in tokens:
            if item.lstrip("-").isdigit():
                tmp_list.append(float(item))
            else:
                num_1 = tmp_list.pop()
                num_2 = tmp_list.pop()
                new_num = eval("%s%s%s" % (num_2, item, num_1))
                tmp_list.append(int(new_num))
                
        if len(tmp_list) == 1:
            return int(tmp_list[0])
        else:
            raise IndexError


if __name__ == "__main__":
    solution = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    target = 0

    print(solution.evalRPN(tokens))
