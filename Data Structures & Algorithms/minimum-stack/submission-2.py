class MinStack:

    def __init__(self):
        self.stack=[]
        self.minn=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.minn or x<=self.minn[-1]:
            self.minn.append(x)
        

    def pop(self) -> None:
        z= self.stack.pop()

        if z==self.minn[-1]:
            self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]
