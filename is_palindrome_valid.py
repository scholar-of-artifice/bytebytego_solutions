def sanitize(s: str) -> str:
    """remove non alpha-numeric characters from a string

    Args:
        s: a string
    Returns:
        a string with all non alpha-numeric characters removed
    """
    #
    # make a new blank string.
    # traverse the input string.
    # is the character alpha-numeric?
    #   if yes, add it to the new string.
    #
    # ANALYSIS
    #   Time
    #       - O(n)
    #       - where n is the length of s.
    #   Space
    #       - O(m)
    #       - where m is the number of alpha numeric characters in s.
    #
    out_s = ''
    for c in s:
        if c.isalnum():
            out_s = out_s + c
    return out_s


def is_palindrome_valid(s: str) -> bool:
    """determines if a string is a palindrome.

    Args:
        s: a string
    Returns:
        true if the string is a palindrome.
        false if the string is NOT a palindrome.
    """
    #
    # ASSUMPTION
    # a string is a palindrome if it can be read the same forwards and backwards.
    #
    # APPROACH 00
    #
    # santize an input string s.
    # compare s with a reversed version of itself.
    #
    # ANALYSIS
    #   TIME
    #       - O(n)
    #       - where n is the length of s.
    #   SPACE
    #       - O(n)
    #       - where n is the length of s.
    #
    s = sanitize(s)
    s_r = ''.join(s[::-1])
    return s == s_r


def is_palindrome_valid(s: str) -> bool:
    """determines if a string is a palindrome.

    Args:
        s: a string
    Returns:
        true if the string is a palindrome.
        false if the string is NOT a palindrome.
    """
    #
    # ASSUMPTION
    # a string is a palindrome if it can be read the same forwards and backwards.
    #
    # APPROACH 01
    #
    # santize an input string s.
    # use 2 pointers that start at opposite ends of the input string.
    # move them inwards.
    # if characters do not match (at any iteration), then s is NOT a palindrome.
    #
    # ANALYSIS
    #   TIME
    #       - O(n)
    #       - where n is the length of s.
    #   SPACE
    #       - O(1)
    #       - the same number of pointers are allocated no matter the size of s.
    #
    s = sanitize(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True
