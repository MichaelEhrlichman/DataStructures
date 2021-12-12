# python3

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
        self.__maxptrstack.pop()
        return self.__stack.pop()

    def Max(self):
        assert(len(self.__maxptrstack))
        return self.__stack[self.__maxptrstack[-1]]

    def __str__(self):
        return ''.join([str(x) for x in self.__stack])

    def __len__(self):
        return len(self.__stack)

def max_sliding_window(sequence, m):
    maximums= []
    a_stk = StackWithMax()
    b_stk = StackWithMax()

    for i in range(m):
        a_stk.Push(sequence.pop(0))
    maximums.append(a_stk.Max())
    for _ in range(len(sequence)):  #each iteration is a window move
        if len(b_stk) == 0:
            while len(a_stk) != 0:
                b_stk.Push(a_stk.Pop())
        b_stk.Pop() #delete leftmost element from window
        a_stk.Push(sequence.pop(0))

        if len(a_stk) > 0:
            a_max = a_stk.Max()
        else:
            a_max = float('-inf')
        if len(b_stk) > 0:
            b_max = b_stk.Max()
        else:
            b_max = float('-inf')
        maximums.append(max(a_max,b_max))
    return maximums


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))

