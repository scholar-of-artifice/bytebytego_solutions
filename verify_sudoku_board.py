from typing import List


def verify_sudoku_board(board: List[List[int]]) -> bool:
    """verify a sudoku board.

    Args:
        board: a 2D list of integers where 0 denotes an unfilled space.
    Returns:
        True if the board is valid, False otherwise.
    """
    #
    # APPROACH 00
    # partition a map for rows, columns and sectors.
    #
    # look at each value in the sudoku board.
    # record all data as you go.
    # if a value occurs in a row_map[row_number] then it is not valid.
    # if a value occurs in a column_map[column_number] then it is not valid.
    # if a value occurs in a sector_map[sector_number] then it is not valid.
    # otherwise it must be valid.
    #
    # ANALYSIS
    #   TIME:
    #     O(n * m)
    #     i must look at every value once.
    #     potentially you could argue that it is O(1) because the sudoku board is a fixed size.
    #   SPACE:
    #     O(n * m)
    #     each data structure must hold (potentially) all data in the sudoku board.
    #
    r_map, c_map, s_map = {}, {}, {}
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            # ignore blank tiles
            if tile == 0:
                continue
            # verify the row
            if i not in r_map:
                r_map.update({i: set()})
            if tile in r_map[i]:
                return False
            else:
                r_map[i].add(tile)
            # verify the column
            if j not in c_map:
                c_map.update({j: set()})
            if tile in c_map[j]:
                return False
            else:
                c_map[j].add(tile)
            # verify the sector
            s = i//3 + (j//3 * 3)
            if s not in s_map:
                s_map.update({s: set()})
            if tile in s_map[s]:
                return False
            else:
                s_map[s].add(tile)
    return True
