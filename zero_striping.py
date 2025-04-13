from typing import List


def find_zeros(matrix: List[List[int]]) -> (set, set):
    """ Identifies all rows and all columns in matrix where the value is 0.

    Args:
        matrix: a 2D list of integers
    Returns:
        a tuple of 2 sets. specifically:
            - a set of row indexes where the value is 0.
            - a set of column indexes where the value is 0.
    """
    # provision a set for row indexes and...
    #   a set for column indexes
    # traverse every element in the input matrix.
    # if a value is 0...
    #   store the row in the row_set
    #   store the column in the column_set
    #
    # ANALYSIS
    #   Time:  O(n * m)
    #       where n is the number of rows and
    #       m is the number of columns
    #   Space: O(n + m)
    #       where n is the number of unique rows where value is 0 and
    #       m is the number of unique columns where value is 0
    #
    r_set, c_set = set(), set()
    for i, row in enumerate(matrix):
        for j, tile in enumerate(row):
            if tile == 0:
                r_set.add(i)
                c_set.add(j)
    return r_set, c_set


def zero_striping(matrix: List[List[int]]) -> None:
    """ Sets the all values which share a row or column index with a value of 0.

    Args:
        matrix: a 2D list of integers
    Returns:
        nothing. mutates matrix.
    """
    # find all columns and rows which have a zero value.
    #
    # ANALYSIS
    #   Time:  O(n * m)
    #       where n is the number of rows and
    #       m is the number of columns
    #   Space: O(n + m)
    #       where n is the number of unique rows where value is 0 and
    #       m is the number of unique columns where value is 0
    #
    # Write your code here
    z_r_set, z_c_set = find_zeros(matrix)
    # loop through sets and overwrite all values in that column of matrix
    for c in z_c_set:
        for i in range(len(matrix)):
            matrix[i][c] = 0
    for r in z_r_set:
        for i in range(len(matrix[r])):
            matrix[r][i] = 0
    return None
