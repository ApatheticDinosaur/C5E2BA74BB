__author__ = 'Andy'


#Node class that contains data and list of child nodes
class Node:
    def __init__(self, data, children=None):
        self.data = data
        if children is None: #Check if children parameter is passed
            self.children = []
        else:
            self.children = children


def levels(root):
    next_level = []
    data = []
    if type(root) is Node: #single child
        data.append(root.data) #gather all data
        next_level = root.children #gather all children nodes
    else:
        for node in root:
            data.append(node.data) #gather all data
            if type(node.children) is Node: #single child
                next_level.append(node.children) #gather all children nodes
            else:
                next_level += node.children
    if next_level == []: #base case, reached the end of the tree
        level = 1
        print("Floor " + str(level) + ":" + str(data))
        return level
    else:
        level = levels(next_level) #recursive function call for the next level
        print("Floor " + str(level) + ":" + str(data))
        return level + 1

a = Node(3, [Node(9, Node(2, Node(8, [Node(1)]))), Node(4, [Node(10), Node(6, Node(7)), Node(5)])])
levels(a)