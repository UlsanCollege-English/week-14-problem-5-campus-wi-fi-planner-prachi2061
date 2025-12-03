import pathlib
import sys

import pytest

THIS_FILE = pathlib.Path(__file__).resolve()
HW_DIR = THIS_FILE.parents[1]
if str(HW_DIR) not in sys.path:
    sys.path.append(str(HW_DIR))

from main import TreeNode, max_level_sum  # noqa: E402


def test_empty_tree():
    assert max_level_sum(None) == (None, 0)


def test_single_node():
    root = TreeNode(10)
    assert max_level_sum(root) == (0, 10)


def test_simple_tree_levels():
    #        5
    #       / \
    #      2   3
    #         / \
    #        4   1
    root = TreeNode(
        5,
        TreeNode(2),
        TreeNode(3, TreeNode(4), TreeNode(1)),
    )
    # Level 0: 5
    # Level 1: 2 + 3 = 5
    # Level 2: 4 + 1 = 5
    # all equal; choose smallest level index -> 0
    assert max_level_sum(root) == (0, 5)


def test_deeper_tree_best_middle_level():
    #       10
    #      /  \
    #     5    7
    #    / \    \
    #   4   1    20
    root = TreeNode(
        10,
        TreeNode(5, TreeNode(4), TreeNode(1)),
        TreeNode(7, None, TreeNode(20)),
    )
    # Level 0: 10
    # Level 1: 5 + 7 = 12
    # Level 2: 4 + 1 + 20 = 25  -> best
    assert max_level_sum(root) == (2, 25)


def test_right_skewed_tree():
    # 3 -> 4 -> 5 -> 6 (all to the right)
    root = TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
    # Each level has one node; best is the level with highest value: 6 at level 3
    assert max_level_sum(root) == (3, 6)


def test_left_heavy_tree():
    #        8
    #       /
    #      3
    #     / \
    #    1   6
    #       / \
    #      4   7
    root = TreeNode(
        8,
        TreeNode(
            3,
            TreeNode(1),
            TreeNode(6, TreeNode(4), TreeNode(7)),
        ),
        None,
    )
    # Level sums:
    # 0: 8
    # 1: 3
    # 2: 1+6 = 7
    # 3: 4+7 = 11 -> best
    assert max_level_sum(root) == (3, 11)


def test_negative_values_allowed():
    #       -1
    #      /  \
    #    -2   -3
    #         /
    #        5
    root = TreeNode(-1, TreeNode(-2), TreeNode(-3, TreeNode(5)))
    # Level 0: -1
    # Level 1: -2 + -3 = -5
    # Level 2: 5
    assert max_level_sum(root) == (2, 5)
