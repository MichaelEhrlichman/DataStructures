# python3
import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

class HashedString:
    m = (10**9 + 7, 10**9 + 9)
    #m = (263130836933693530167218012159999999,8683317618811886495518194401279999999)
    #m = (31,107)
    x = 126
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


def LongestMatch(ha,hb,kmin0,kmax0):
    # assume ha, hb sorted such that len(ha) <= len(hb)
    kmin,kmax = kmin0,kmax0
    ifound,jfound,kfound = 0,0,0
    while True:
        k = kmin + (kmax-kmin)//2 + 1
        ha_hash_table_0 = dict([(ha.HashAK(i,k,0) , i) for i in range(ha.n-k+1)])
        for j in range(hb.n-k+1):
            hb_hash = hb.HashAK(j,k,0) 
            if hb_hash in ha_hash_table_0:
                i = ha_hash_table_0[hb_hash]
                ha_hash = ha.HashAK(i,k,1) 
                hb_hash = hb.HashAK(j,k,1) 
                if ha_hash == hb_hash:
                    ifound = i
                    jfound = j
                    kfound = k
                    kmin = k
                    break
        else:
            kmax = k-1
            if kmax <= kmin:
                return Answer(ifound,jfound,kfound)
        if kmax < kmin:
            return Answer(ifound,jfound,kfound)

for line in sys.stdin.readlines():
    s_in, t_in = line.split()
    hs = HashedString(s_in)
    ht = HashedString(t_in)
    if len(s_in) <= len(t_in):
        ans = LongestMatch(hs,ht,0,hs.n-1)
        print(ans.i, ans.j, ans.len)
    else:
        ans = LongestMatch(ht,hs,0,ht.n-1)
        print(ans.j, ans.i, ans.len)
