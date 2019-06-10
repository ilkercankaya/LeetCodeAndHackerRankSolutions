# Is This a Binary Search Tree?

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def get_in_order_list(root, list_in):
    if root != None:
        get_in_order_list(root.left, list_in)
        list_in.append(root.data)
        get_in_order_list(root.right, list_in)


def check_binary_search_tree_(root):
    in_order = []
    get_in_order_list(root, in_order)

    for i in range(len(in_order)):
        if i + 1 < len(in_order) and in_order[i] >= in_order[i + 1]:
            return False

    return True
