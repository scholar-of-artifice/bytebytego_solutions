from typing import List


def calculate_area(w: int, h: int) -> int:
    """compute the area of a 2D rectangle.

    Args:
        width: an integer
        heights: an integer
    Returns:
        an integer
    """
    return w*h


def largest_container(heights: List[int]) -> int:
    """find the largest 2D area given an array of height values.

    Args:
        heights: an un/sorted list of integers
    Returns:
        an integer
    """
    # en
    #
    # ASSUMPTION
    # - the input list can be empty
    # - values can be negative
    # examples of expected behaviour:
    #     nums: [] => 0
    #     nums: [1] => 0
    #     nums: [1, -3] => 0
    #     nums: [1, 3] => 1
    #
    # APPROACH 00
    # create a variable to store the maximum observed height.
    # use 2 pointers starting from opposite ends.
    # traverse the array.
    # at each value, compute the area of the container.
    #   width is the distance between the pointers.
    #   height is the min height value at those two pointers.
    # overwrite the maximum observed height with the appropriate area value.
    # move lagging pointer forward if it is shorter.
    # -or- move leading pointer backward if it is shorter.
    #   why? because height is determined by the min of these height values.
    #
    # ANALYSIS
    #   TIME:
    #     O(n)
    #     i must look at every value in the array at least once
    #   SPACE:
    #     O(1)
    #     i allocate the same number of variables no matter the size of the input.
    #
    largest_container_size = 0
    i, j = 0, len(heights) - 1
    while i < j:
        a, b = heights[i], heights[j]
        w, h = abs(j - i), min(a, b)
        area = calculate_area(w, h)
        largest_container_size = max(largest_container_size, area)
        if a <= b:
            i = i + 1
        else:
            j = j - 1
    return largest_container_size
