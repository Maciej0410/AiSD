from typing import List, Callable, Any
import copy
from binarytree import Node




class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


    def __repr__(self):
        return str(self.value)

    def is_leaf(self):
        return self.leftChild == self.rightChild == None

    def add_left_child(self, value):
        self.leftChild = BinaryNode(value)

    def add_right_child(self, value):
        self.rightChild = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.leftChild != None:
            self.leftChild.traverse_in_order(visit)
        visit(self)
        if self.rightChild != None:
            self.rightChild.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.leftChild != None:
            self.leftChild.traverse_post_order(visit)
        if self.rightChild != None:
            self.rightChild.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.leftChild != None:
            self.leftChild.traverse_pre_order(visit)
        if self.rightChild:
            self.rightChild.traverse_pre_order(visit)




class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if type(self) == BinaryTree:
            if self.root.leftChild != None:
                self.root.leftChild.traverse_in_order(visit)
            visit(self.root)
            if self.root.rightChild != None:
                self.root.rightChild.traverse_in_order(visit)
        if type(self) == BinaryNode:
            if self.leftChild != None:
                self.leftChild.traverse_in_order(visit)
            visit(self)
            if self.rightChild != None:
                self.rightChild.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if type(self) == BinaryTree:
            if self.root.leftChild != None:
                self.root.leftChild.traverse_post_order(visit)
            if self.root.rightChild != None:
                self.root.rightChild.traverse_post_order(visit)
            visit(self.root)
        if type(self) == BinaryNode:
            if self.leftChild != None:
                BinaryTree.traverse_post_order(visit)
            if self.rightChild != None:
                BinaryTree.traverse_post_order(visit)
            visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        if type(self) == BinaryTree:
            visit(self.root)
            if self.root.leftChild != None:
                self.root.leftChild.traverse_pre_order(visit)

            if self.root.rightChild != None:
                self.root.rightChild.traverse_pre_order(visit)

        if type(self) == BinaryNode:
            visit(self)
            if self.leftChild != None:
                BinaryTree.traverse_pre_order(visit)
            if self.rightChild != None:
                BinaryTree.traverse_pre_order(visit)





def depth_first_search(node: BinaryNode, current_result: List[List[BinaryNode]], current_path: List[BinaryNode]):
    current_path.append(node)
    if node.is_leaf():
        current_result += [copy.deepcopy(current_path)]

    for neib in [node.rightChild, node.leftChild]:
        if neib != None:
            depth_first_search(neib, current_result, current_path)

    current_path.pop()


def all_paths(tree: BinaryTree) -> List[List[BinaryNode]]:
    current_path = []
    current_result = []
    depth_first_search(tree.root, current_result, current_path)

    return current_result


def wyswietl(node: 'BinaryNode'):
    print(node.value)


if __name__ == '__main__':
    n1 = BinaryNode(1)
    n2 = BinaryNode(2)
    n3 = BinaryNode(3)
    n4 = BinaryNode(4)
    n5 = BinaryNode(5)
    n7 = BinaryNode(7)
    n8 = BinaryNode(8)
    n9 = BinaryNode(9)

    n1.leftChild = n2
    n1.rightChild = n3
    n2.leftChild = n4
    n2.rightChild = n5
    n4.leftChild = n8
    n4.rightChild = n9
    n3.rightChild = n7

    tree = BinaryTree(n1)
    assert tree.root.value == 1
    assert tree.root.rightChild.value == 3
    assert tree.root.rightChild.is_leaf() is False
    assert tree.root.rightChild.rightChild.is_leaf() is True

    print(all_paths(tree))

    print("\n")
    tree.traverse_in_order(wyswietl)
    print("\n")
    tree.traverse_post_order(wyswietl)
    print("\n")
    tree.traverse_pre_order(wyswietl)
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.left.left=Node(8)
    root.left.left.right=Node(9)
    root.left.right=Node(5)
    root.right.right=Node(7)
    print(root)

