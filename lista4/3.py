from random import random


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data) + ':  [' + ', '.join(map(str, self.children)) + ']'

    @staticmethod
    def random_tree(height, child_probability):
        node_number = 1

        def random_subtree(height):
            nonlocal node_number
            nonlocal child_probability

            node_number += 1
            tree = Node(str(node_number))

            if height > 0:
                while random() < child_probability:  # nooo you can't just randomly generate subtrees
                    tree.children.append(random_subtree(height - 1)) # haha tree machine goes brrrrr

            return tree

        tree = Node(str(node_number))
        curr = tree

        while height > 0:
            node_number += 1
            height -= 1

            while random() < child_probability/2:  # possible subtrees before base height
                curr.children.append(random_subtree(height))

            newCurr = Node(str(node_number))  # base height subtree
            curr.children.append(newCurr)

            while random() < child_probability/2:  # possible subtrees after base height
                curr.children.append(random_subtree(height))

            curr = newCurr

        return tree        

def dfs(tree: Node):
    if tree is not None:
        yield tree.data
        for child in tree.children:
            yield from dfs(child)

def bfs(tree: Node):
    q: List[Node] = [tree]
    while len(q) > 0:
        current = q.pop(0)
        for child in current.children:
            q.append(child)
        yield current.data

t = Node.random_tree(3, 0.8)
print(str(t))
print(list(dfs(t)))
print(list(bfs(t)))