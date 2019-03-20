"""Python Script to practice my ability to code in the language
as well as refresh my ability to code basic data structures from scratch!"""


class Node:

    # The option to initialize with just data or with pre-existing child nodes
    def __init__(self, data, l_node=None, r_node=None):
        self.data = data
        self.l_node = l_node
        self.r_node = r_node

    def get_data(self):
        return self.data

    def get_l_node(self):
        return self.l_node

    def get_r_node(self):
        return self.r_node

    # Check if this node is a leaf of the tree
    def check_leaf_node(self) -> bool:
        if self.l_node is None and self.r_node is None:
            return True
        else:
            return False

    # Adds new node to the tree starting with the root
    def add_node(self, new_data):
        if self.data > new_data:
            if self.l_node is None:
                self.l_node = Node(new_data)
            else:
                self.l_node.add_node(new_data)
        elif self.data < new_data:
            if self.r_node is None:
                self.r_node = Node(new_data)
            else:
                self.r_node.add_node(new_data)
        return

    # Prints the tree
    def print_tree(self):
        if self.l_node:
            self.l_node.print_tree()
        print(self.data)
        if self.r_node:
            self.r_node.print_tree()

    def nice_print_tree(self):
        return


# Build a Binary Tree
def main():
    data_list = [1, 2, 3, 49, 14, 93, 65, 100, 77, 32]
    root = Node(0)
    for i in range(len(data_list)):
        # print(data_list[i])
        root.add_node(data_list[i])
    root.print_tree()
    return


if __name__ == "__main__":
    main()
