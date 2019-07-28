# _*_ coding=utf-8 _*_


"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


def search_matrix(matrix, target):
    """
    直接循环查找，线性查找，时间复杂度度O(n)
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for i in matrix:
        if target in i:
            return True

    return False


def search_matrix_mid(matrix, target):
    """
    二分查找，时间复杂度O(longn)
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """
    h = len(matrix)
    if h == 0:
        return False

    w = len(matrix[0])
    if w == 0:
        return False

    left = 0
    right = w * h - 1
    while left <= right:
        mid = (left + right) // 2
        i = mid // w                     # 元素所在的那一行
        j = mid % w                      # 元素所在的那一列
        if target == matrix[i][j]:
            return True
        elif target < matrix[i][j]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False
