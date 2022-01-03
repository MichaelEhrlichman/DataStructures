# python3

from sys import stdin
#import graphics as gr

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)
  def __str__(self):
    selfleftkey, selfrightkey, selfparentkey = -1, -1, -1
    if self.left != None:
        selfleftkey = self.left.key
    if self.right != None:
      selfrightkey = self.right.key
    if self.parent != None:
      selfparentkey = self.parent.key
    return 'Vertex(key='+str(self.key)+', sum='+str(self.sum)+', leftkey='+str(selfleftkey)+ \
           ', rightkey='+str(selfrightkey)+', parentkey='+str(selfparentkey)+')'

def update(v):
  #update sum based on .left and .right
  #set .left and .right parent to v
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:  #v is on the left of its parent
    m = v.right
    v.right = parent
    parent.left = m
  else:  # v is on the right of its parent
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(key): 
  global root
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  if next:
    root = splay(next)
  return next

def split(node,key):  
  result = find(key)  
  if result == None:    
    return (node, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right
  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)

def LeftDescendant(x):
  if x.left == None:
    return x
  else:
    return LeftDescendant(x.left)

def RightAncestor(N):
  if N.parent == None:
    return None
  if N.key < N.parent.key:
    return N.parent
  else:
    return RightAncestor(N.parent)

def stnext(N):
  if N.right:
    return LeftDescendant(N.right)
  else:
    return RightAncestor(N)

def delete(N):
  if N.left == None and N.right == None:
    #N is the only node in the tree
    root = None
    return None
  elif N.right == None:
    #if N is largest node in the tree, then it has no right descendent
    N.left.parent = None
    return N.left
  elif N.left == None:
    #deleting smallest node in the tree, no left descendant
    N.right.parent = None
    return N.right
  else:
    #we are here because N is neither smallest nor largest node in the tree
    N.right.left = N.left
    N.left.parent = N.right
    N.right.parent = None
    return N.right

def erase(x):
  global root
  N = find(x) #find node without splay
  if N and N.key == x:
    (left,right) = split(root,x)
    (middle,right) = split(right,x+1)
    root = merge(left,right)
  
#def olderase(x): 
#  global root
#  N = find(x,do_splay=False) #find node without splay
#  if N and N.key == x:
#    if root == N:
#      root = delete(N)
#    elif N != None:
#      mynext = stnext(N)
#      if mynext:
#        root = splay(mynext)
#      root = splay(N)
#      root = delete(N)

def search(x): 
  global root
  N = find(x) #the find operation already includes a splay at the end
  if N == None:
    return False
  return True if x==N.key else False
  
def sum(fr, to): 
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  if middle:
    ans = middle.sum
  else:
    ans = 0
  root = merge(merge(left, middle), right)
  return ans

#def tree_height(node):
#  if node.left and node.right:
#    return 1+max(tree_height(node.left),tree_height(node.right)) 
#  elif node.left:
#    return 1+tree_height(node.left)
#  elif node.right:
#    return 1+tree_height(node.right)
#  else:
#    return 0
#
#winx,winy = 1900,500
#csize = 20
#row_height = 50
#col_sep = 45
#
#def draw_node(win,loc,node,height):
#  cir = gr.Circle(loc,csize)
#  cir_txt = gr.Text(loc,str(node.key)+'\n'+str(node.sum))
#  cir.draw(win)
#  cir_txt.draw(win)
#  if node.left:
#    newloc = gr.Point(loc.x-col_sep*height,loc.y+row_height)
#    x = (loc.y-newloc.y)/(loc.x-newloc.x)
#    lsinangle = csize * x / (1+x*x)**0.5
#    lcosangle = csize / (1+x*x)**0.5
#    edge = gr.Line(gr.Point(loc.x-lcosangle,loc.y-lsinangle), gr.Point(newloc.x+lcosangle,newloc.y+lsinangle))
#    edge.draw(win)
#    draw_node(win,newloc,node.left,height-1)
#  if node.right:
#    newloc = gr.Point(loc.x+col_sep*height,loc.y+row_height)
#    x = (loc.y-newloc.y)/(loc.x-newloc.x)
#    lsinangle = csize * x / (1+x*x)**0.5
#    lcosangle = csize / (1+x*x)**0.5
#    edge = gr.Line(gr.Point(loc.x+lcosangle,loc.y+lsinangle), gr.Point(newloc.x-lcosangle,newloc.y-lsinangle))
#    edge.draw(win)
#    draw_node(win,newloc,node.right,height-1)
#
#def gr_tree(root,title='Tree',save=False):
#  win = gr.GraphWin(title,winx,winy)
#  if root:
#    height = tree_height(root)
#    draw_node(win,gr.Point(winx//2,row_height),root,height)
#  win.getMouse()
#  if not save:
#    win.close()

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    #print('   insert '+str((x+last_sum_result)%MODULO))
    #print(line)
    #gr_tree(root)
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    #print('   erase '+str((x+last_sum_result)%MODULO))
    #print(line)
    #gr_tree(root)
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    #print('   search '+str((x+last_sum_result)%MODULO))
    #print(line)
    #gr_tree(root)
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    #print('   sum '+str((l+last_sum_result)%MODULO)+' '+str((r+last_sum_result)%MODULO))
    #print(line)
    #gr_tree(root)
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO
#gr_tree(root)
