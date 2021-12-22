# python3

import sys

class HashedString:
    m = (10**9 + 7, 10**9 + 9)
    #m = (263130836933693530167218012159999999,8683317618811886495518194401279999999)
    x = 453
    xkm_cache = [[None for _ in range(100001)] for _ in range(len(m))]

    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.h = []
        for mix in range(len(self.m)):
            self.MakeRollingCache(mix)

    def MakeRollingCache(self,mix):
        self.h.append([0 for _ in range(self.n+1)])
        for i in range(1,self.n+1):
            self.h[mix][i] = (self.x * self.h[mix][i-1] + ord(self.s[i-1])) % self.m[mix]
        return None

    def HashAK(self,a,k,mix):
        if self.xkm_cache[mix][k] == None:
            self.xkm_cache[mix][k] = pow(self.x, k, self.m[mix])
        return (self.h[mix][a+k] % self.m[mix] - self.xkm_cache[mix][k] * self.h[mix][a]%self.m[mix]) % self.m[mix]

def check_equal(h1,a1,h2,a2,k):
    if h1.HashAK(a1,k,0) == h2.HashAK(a2,k,0):
        if h1.HashAK(a1,k,1) == h2.HashAK(a2,k,1):
            return True
    return False

def solve(k, text, pattern):
    ht = HashedString(text)
    hp = HashedString(pattern)
    matches = []
    for i in range(ht.n - hp.n + 1):
        k = hp.n
        at = i
        ap = 0
        if check_equal(ht,at,hp,ap,k):
            matches.append(i)
        else:
            while True:
                l = k - k//2 
                k = k//2
                check_equal(ht,at,hp,0,k)
                check_equal(ht,at+l,hp,0,l)
	return matches

for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
