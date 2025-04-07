from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    """move all 0s to the end of the list and preserve the relative order of other values.

    Args:
        nums: a list of integers
    Returns:
        nothing. mutate the old list.
    """
    # APPROACH 00
    # create 2 lists (a, b) to hold values from nums.
    # for each value in nums...
    #   if value is not 0 write to a
    #   if value is 0 write to b
    # merge the new lists
    # overwrite the old list the new list
    #
    # ANALYSIS
    #   Time:  O(n)
    #   Space: O(n)
    #
    L_a, L_b = [], []
    for n in nums:
        if n == 0:
            L_b = L_b + [n]
        else:
            L_a = L_a + [n]
    nums[:] = L_a + L_b
    return None
