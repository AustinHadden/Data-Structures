from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        def find_insert_place(current_node, value):
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BinarySearchTree(value)
                    return
                else:
                    return find_insert_place(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = BinarySearchTree(value)
                    return
                else:
                    return find_insert_place(current_node.right, value)

        find_insert_place(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def find_value(current_node, target):
            if current_node.value == target:
                return True
            if target < current_node.value:
                if current_node.left is not None:
                    return find_value(current_node.left, target)
            if target >= current_node.value:
                if current_node.right is not None:
                    return find_value(current_node.right, target)

            return False

        return find_value(self, target)

    # Return the maximum value found in the tree
    def get_max(self):
        def get_max_node(current_node):
            if current_node.right is None:
                return current_node
            else:
                return get_max_node(current_node.right)

        return get_max_node(self).value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def do_cb(current_node, cb):
            cb(current_node.value)
            if current_node.left:
                do_cb(current_node.left, cb)
            if current_node.right:
                do_cb(current_node.right, cb)

        do_cb(self, cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
