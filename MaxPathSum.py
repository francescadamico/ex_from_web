'''
https://igotanoffer.com/blogs/tech/google-software-engineer-interview

Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.
'''


class Node:
  
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def visit(n, summ):
  
  new_summ = summ + n.data
  
  if new_summ < 0:   
    return summ
  else:
    return new_summ

def max_path_sum(n, summ = 0, max_summ = 0):
  
  new_summ = visit(n, summ)

  if any([n.left == None and n.right == None, new_summ == summ]):
    max_summ = new_summ if new_summ > max_summ else max_summ
    new_summ = 0
  
  if n.left != None:
    max_summ = max_path_sum(n.left, new_summ, max_summ)
  if n.right != None:  
    max_summ = max_path_sum(n.right, new_summ, max_summ)

  return max_summ




n1 = Node(1)
n2 = Node(6)
n3 = Node(-3)
n4 = Node(5)
n5 = Node(4)
n6 = Node(2)
n7 = Node(-9)
n8 = Node(4)
n9 = Node(8)
n10 = Node(5)
n11 = Node(-7)

n1.left = n2
n2.left = n3
n3.left = n4
n3.right = n5
n2.right = n6
n6.right = n7
n1.right = n8
n8.left = n9
n8.right = n10
n10.right = n11

print(max_path_sum(n1))



