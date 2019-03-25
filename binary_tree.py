"""Python Script to practice my ability to code in the language
as well as refresh my ability to code basic data structures from scratch!"""

import queue
import math


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

    # Traverse Tree breadth wise and return a list, in breadth order
    def travers_breadth_first(self):
        visited_nodes = [self.data]
        q = queue.queue()
        q.add_to_queue(self)
        while q.queue_list is not None:
            curr_node = q.pop_queue()
            if curr_node.l_node is not None:
                q.add_to_queue(curr_node.l_node)
                visited_nodes.append(curr_node.l_node.data)
            else:
                visited_nodes.append("N/a")
            if curr_node.r_node is not None:
                q.add_to_queue(curr_node.r_node)
                visited_nodes.append(curr_node.r_node.data)
            else:
                visited_nodes.append("N/a")
        return visited_nodes

    # Prints the tree
    def print_tree(self):
        if self.l_node:
            self.l_node.print_tree()
        print(self.data)
        if self.r_node:
            self.r_node.print_tree()

    # Prints the tree to look similar to it's actual representation, via Breadth First
    def nice_print_tree(self):
        exponent = 0
        visited_nodes = self.travers_breadth_first()
        while visited_nodes is not None:
            level_range = 2 ** exponent
            if level_range > len(visited_nodes):
                # print rest of visited nodes since this level is not full, and therefore the bottom
                print("Level: " + str(visited_nodes))
                print("Depth: " + str(exponent))
                return
            else:
                # Build level to print
                level_list = visited_nodes[0:level_range]
                # Prune levels off and update list
                visited_nodes = visited_nodes[level_range:]
                print("Level: " + str(level_list))
                if 0 < visited_nodes.count("N/a") == len(visited_nodes):
                    print("Depth: " + str(exponent))
                    return
                exponent = exponent + 1
                if len(visited_nodes) == 0:
                    print("Depth: " + str(exponent))
                    return
        return


# Build a Binary Tree
def main():
    data_list = [-1, 1, -2, 2, -3, 3, -3, 4, -5, 5, -6, 6, -7, 7]
    root = Node(0)
    for i in range(len(data_list)):
        root.add_node(data_list[i])
        root.nice_print_tree()
        print("============================")
    # root.print_tree()
    # root.nice_print_tree()
    return


if __name__ == "__main__":
    main()
