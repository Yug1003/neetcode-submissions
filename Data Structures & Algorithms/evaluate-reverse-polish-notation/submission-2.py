class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []

        for i in tokens:
            if i in "+-*/":
                b = lst.pop()
                a = lst.pop()

                if i == '+':
                    lst.append(a + b)
                elif i == '-':
                    lst.append(a - b)
                elif i == '*':
                    lst.append(a * b)
                else:
                    lst.append(int(a / b))
            else:
                lst.append(int(i))

        return lst[-1]