from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    """find the indexes in nums which sum to target.

    Args:
        nums: a sorted list of integers
        target: an integer
    Returns:
        a list of length 2. if no pair of indexes is found then list will be blank
    """
    # Write your code here
    #
    # ASSUMPTION
    # the returned list must have unique indexes
    # # example (not accepted) -> nums: [1, 2], target: 4 => [1, 1]
    #
    # APPROACH 00
    # use 2 ptr starting from opposite ends
    i, j = 0, len(nums) - 1
    # move these ptr towards the center
    # for each given pair of points
    while i < j:
        # # calculate the sum
        s = nums[i] + nums[j]
        # #if the sum is target -> return the pair
        if s == target:
            return [i, j]
        # # if the sum is not the target
        else:
            # # # is the sum less than the target?
            # # # // is the sum greater than the target?
            if s < target:
                # # # # move the lagging ptr up
                i = i + 1
            else:
                # # # # move the leading ptr down
                j = j - 1
    #
    # Complexity
    # TIME: O(n):
    # # we must look at every value in the array at least once
    # SPACE: O(1):
    # # we only allocate the pointers and array of fixed size for return
    return []
