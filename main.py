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
        self.value = value
        self.left = left
        self.right = right


def max_level_sum(root):
    """
    Return (best_level_index, best_sum) where best_level_index is the level
    with the highest sum of node values, and best_sum is that sum.

    For an empty tree (root is None), return (None, 0).
    """
    if root is None:
        return (None, 0)

    queue = [root]
    level = 0
    best_level = 0
    best_sum = root.value  # root is level 0

    while queue:
        next_queue = []
        current_sum = 0

        for node in queue:
            current_sum += node.value
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

        # update best if needed
        if current_sum > best_sum:
            best_sum = current_sum
            best_level = level

        queue = next_queue
        level += 1

    return (best_level, best_sum)


if __name__ == "__main__":
    left = TreeNode(5, TreeNode(4), TreeNode(1))
    right = TreeNode(7)
    root = TreeNode(10, left, right)
    print(max_level_sum(root))
