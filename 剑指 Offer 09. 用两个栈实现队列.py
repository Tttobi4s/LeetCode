class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        else:
            while self.A:
                self.B.append(self.A.pop())
        return self.B.pop() if self.B else -1

    def appendTail(self, value: int) -> None:
        self.A.append(value)