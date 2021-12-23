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
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,ix=0):
    if self.left[ix] > -1:
        _ = self.inOrder(self.left[ix])
    self.result.append(self.key[ix])
    if self.right[ix] > -1:
        _ = self.inOrder(self.right[ix])
                
    return self.result

  def preOrder(self,ix=0):
    self.result.append(self.key[ix])
    if self.left[ix] > -1:
        _ = self.preOrder(self.left[ix])
    if self.right[ix] > -1:
        _ = self.preOrder(self.right[ix])
                
    return self.result

  def postOrder(self,ix=0):
    if self.left[ix] > -1:
        _ = self.postOrder(self.left[ix])
    if self.right[ix] > -1:
        _ = self.postOrder(self.right[ix])
    self.result.append(self.key[ix])
                
    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    tree.result = []
    print(" ".join(str(x) for x in tree.preOrder()))
    tree.result = []
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
