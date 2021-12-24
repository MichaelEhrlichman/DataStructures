# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.result = [] 
    self.fail = False
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def isBST(self,ix=0):
    if self.left[ix] > -1:
        if self.key[self.left[ix]] >= self.key[ix]:
            self.fail = True
        self.isBST(self.left[ix])
    self.result.append(self.key[ix])
    if self.right[ix] > -1:
        if self.key[self.right[ix]] < self.key[ix]:
            self.fail = True
        self.isBST(self.right[ix])
                
    if ix==0:
        return not self.fail and all([ (self.result[j]<=self.result[j+1]) for j in range(self.n-1)])

def main():
    tree = TreeOrders()
    tree.read()
    if len(tree.key) == 0:
        print('CORRECT')
    elif tree.isBST():
        print('CORRECT')
    else:
        print('INCORRECT')
    #print(tree.result)

threading.Thread(target=main).start()
