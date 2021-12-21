# python3
import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

class HashedString:
    m = []
    m.append(10**9 + 7)
    m.append(10**9 + 9)
    x = 345
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.h1, self.h2 = self.HashCache()

    def HashCache(self):
        h1 = [0 for _ in range(self.n+1)] 
        h2 = [0 for _ in range(self.n+1)] 
        for i in range(1,self.n+1):
            h1[i] = (self.x * h1[i-1] + ord(self.s[i-1])) % self.m[0]
            h2[i] = (self.x * h2[i-1] + ord(self.s[i-1])) % self.m[1]
        return h1, h2

    def HashAK(self,a,k,mix):
        xkm = pow(self.x, k, self.m[mix])
        return (self.h1[a+k] % self.m[mix] - xkm * self.h1[a]%self.m[mix])

	return Answer(i, j, l)

def LongestMatch(ha,hb):
    # assume ha, hb sorted such that len(ha) <= len(hb)
    k = len(ha)//2
    for i in range(len(ha)-k):
        ha_hash = ha.HashAK(i,k,1) 
        for j in range(len(hb)-k):
            hb_hash = hb.HashAK(j,k,1) 
            if ha_hash == hb_hash:
                ha_hash = ha.HashAK(i,k,2) 
                hb_hash = hb.HashAK(j,k,2) 
                if ha_hash == hb_hash:
                    LongestMatch(
                else:
                
    

for line in sys.stdin.readlines():
	s_in, t_in = line.split()
    hs = HashedString(s_in)
    ht = HashedString(t_in)
    if len(s_in) <= len(t_in):
        ans = LongestMatch(hs,ht)
	    print(ans.i, ans.j, ans.len)
    else:
        ans = LongestMatch(ht,hs)
	    print(ans.j, ans.i, ans.len)
