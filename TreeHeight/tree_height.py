# python3

import sys
import threading

def naive_compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def make_tree(parents):
    tree = [ [] for _ in range(len(parents))]
    for c,p in enumerate(parents):
        if p > -1:
            tree[p].append([c])
        elif p == -1:
            head = c
    return tree, head

def height(tree,head):
    if not tree:
        return 0
    #print("head:")
    #print(head)
    if not tree[head]:
        return 1
    branches = [height(tree,br[0]) for br in tree[head]]
    return 1 + max(branches)

def test_main():
    for i in range(1,24):
        test = '{:02}'.format(i)
        answer = '{:02}.a'.format(i)
        with open('tests/'+test,'r') as tf, open('tests/'+answer,'r') as af:
            n = int(tf.readline())
            parents = list(map(int,tf.readline().split()))
            ansstr = int(af.read().strip())
            tree,head = make_tree(parents)
            print(test)
            assert height(tree,head) == ansstr

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree,head = make_tree(parents)
    #print(tree,head)
    print(height(tree,head))
    #print(naive_compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**28)   # new thread will get stack of such size
threading.Thread(target=main).start()
