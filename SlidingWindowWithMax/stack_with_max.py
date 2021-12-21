#python3
import sys

class naive_StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__maxptrstack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__maxptrstack) == 0:
            self.__maxptrstack.append(0)
        else:
            if self.__stack[-1] > self.__stack[self.__maxptrstack[-1]]:
                self.__maxptrstack.append(len(self.__stack)-1)
            else:
                self.__maxptrstack.append(self.__maxptrstack[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__maxptrstack.pop()

    def Max(self):
        assert(len(self.__maxptrstack))
        return self.__stack[self.__maxptrstack[-1]]

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
