class MinStack:

    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B:
            self.B.append(x)
        else:
            if x <= self.B[-1]:
                self.B.append(x)

    def pop(self) -> None:
        x = self.A.pop()
        if x == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1] if self.B else -1
