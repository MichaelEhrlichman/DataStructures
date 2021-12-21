# python3

import sys

class Solver:
    m1 = 10**9 + 7
    m2 = 10**9 + 9
    x = 584738
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.h1, self.h2 = self.HashCache()

    def HashCache(self):
        h1 = [0 for _ in range(self.n+1)] 
        h2 = [0 for _ in range(self.n+1)] 
        for i in range(1,self.n+1):
            h1[i] = (self.x * h1[i-1] + ord(self.s[i-1])) % self.m1
            h2[i] = (self.x * h2[i-1] + ord(self.s[i-1])) % self.m2
        return h1, h2

    def CheckEqual(self,a,b,l):
        xlm = pow(self.x, l, self.m1)
        Ha1 = (self.h1[a+l] % self.m1 - xlm * self.h1[a]%self.m1)
        Hb1 = (self.h1[b+l] % self.m1 - xlm * self.h1[b]%self.m1)
        if Ha1%self.m1 == Hb1%self.m1:
            xlm = pow(self.x, l, self.m2)
            Ha2 = (self.h2[a+l] % self.m2 - xlm * self.h2[a]%self.m2)
            Hb2 = (self.h2[b+l] % self.m2 - xlm * self.h2[b]%self.m2)
            if Ha2%self.m2 == Hb2%self.m2:
                return True
        return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.CheckEqual(a, b, l) else "No")
