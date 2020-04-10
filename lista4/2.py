from random import random

def radnom_tree(height):
    node_number = 1

    def random_subtree(max_height): # recursively generates random subtree
        nonlocal node_number
        if random() > 0.5 or height == 0:
            return None
        node_number += 1
        tree = [str(node_number), None, None]
        if random() > 0.5: # left subtree
            tree[1] = random_subtree(height - 1)
        if random() > 0.5: # right subtree
            tree[2] = random_subtree(height - 1)

        return tree

    tree = [str(node_number), None, None]
    curr = tree
    
    while height > 0: # guarantee main tree height
        node_number += 1
        height -= 1
        if random() > 0.5: # going left
            curr[1] = [str(node_number), None, None]
            curr[2] = random_subtree(height)
            curr = curr[1]
        else: # going right
            curr[2] = [str(node_number), None, None]
            curr[1] = random_subtree(height)
            curr = curr[2]

    return tree

def dfs(tree):
    if tree is not None:
        yield tree[0]
        yield from dfs(tree[1])
        yield from dfs(tree[2])

def bfs(tree):
    q = [tree]
    while len(q) > 0:
        current = q.pop(0)
        if current[1] is not None:
            q.append(current[1])
        if current[2] is not None:
            q.append(current[2])
        yield current[0]

t = radnom_tree(3)
print(t)
print(list(dfs(t)))
print(list(bfs(t)))