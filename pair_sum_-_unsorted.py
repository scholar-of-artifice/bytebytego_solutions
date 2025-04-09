from typing import List


def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    """find the indexes in nums which sum to target.

    Args:
        nums: an un/sorted list of integers
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
    # use a map/dict/associative container.
    # traverse the array.
    # at each value, compute the complement.
    # query the map for the complement.
    # if complement is observed in map:
    #   return the indexes
    # else
    #   store in the map {value_at_current_position : index}
    #
    # ANALYSIS
    #   TIME:
    #     O(n)
    #     I must look at every value in the array at least once
    #   SPACE:
    #     O(n)
    #     in the worst case, the map will be the same size as the input array
    #
    observations_map = {}
    for i, v in enumerate(nums):
        complement = target - v
        if complement in observations_map:
            return [observations_map[complement], i]
        else:
            observations_map.update({v: i})
    return []
