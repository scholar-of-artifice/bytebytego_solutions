from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    """find the indexes in nums which sum to target.

    Args:
        nums: a sorted list of integers
        target: an integer
    Returns:
        a list of length 2. if no pair of indexes is found then list will be blank
    """
    # en
    #
    # ASSUMPTION
    # - the returned list must have unique indexes.
    # examples of expected behaviour:
    #     nums: [1, 2], target: 4 => []
    #     nums: [-1, 2], target: 1 => [0, 1]
    # examples of not expected behaviour:
    #     nums: [1, 2], target: 4 => [1, 1]
    #
    # APPROACH 00
    # use 2 pointers starting from opposite ends.
    # move these pointers towards the center.
    # calculate the sum for each given pair of points.
    # if the sum is the target -> return the pair
    # if the sum is not the target
    #   is the sum less than the target?
    #       move the lagging ptr up
    #   is the sum greater than the target?
    #       move the leading ptr down
    #
    # ANALYSIS
    #   TIME:
    #     O(n)
    #     I must look at every value in the array at least once
    #   SPACE:
    #     O(1)
    #     I only allocate the pointers and an array of fixed size to return
    #
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [i, j]
        else:
            if s < target:
                i = i + 1
            else:
                j = j - 1
    return []
