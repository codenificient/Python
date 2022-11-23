class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def prinTree(node, level = 0):
    if node != None:
        prinTree(node.left, level + 1)
        print(" " * 5 * level + str(node.data))
        prinTree(node.right, level + 1)


def CreateMinTree(arr, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    trees = TreeNode(arr[mid])
    trees.left = CreateMinTree(arr, start, mid - 1)
    trees.right = CreateMinTree(arr, mid + 1, end)
    return trees


if __name__ == "__main__":
    t = CreateMinTree([3, 1, 4, 9, 20, 31, 76], 0, 6)
    prinTree(t)
