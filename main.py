
## main.py
```python
"""
HW05 — Campus Wi-Fi Planner (Max Level Load in a Tree)

Implement TreeNode and max_level_sum(root) to find the level with the highest
total capacity in a binary tree.
"""


class TreeNode:
    """
    Binary tree node for Wi-Fi routers.

    value: integer capacity
    left, right: TreeNode or None
    """

    def __init__(self, value, left=None, right=None):
        # TODO: store the fields on the instance
        pass


def max_level_sum(root):
    """
    Return (best_level_index, best_sum) where best_level_index is the level
    with the highest sum of node values, and best_sum is that sum.

    For an empty tree (root is None), return (None, 0).
    """
    # TODO (8 Steps of Coding, minimal prompts):
    # - Design a BFS (level-order) traversal using a queue.
    # - Track current level index, sum per level, and the best level so far.
    # - Handle the empty tree case.
    raise NotImplementedError("Implement max_level_sum in main.py")


if __name__ == "__main__":
    # Optional manual tree:
    #       10
    #      /  \
    #     5    7
    #    / \
    #   4   1
    left = TreeNode(5, TreeNode(4), TreeNode(1))
    right = TreeNode(7)
    root = TreeNode(10, left, right)
    print(max_level_sum(root))
