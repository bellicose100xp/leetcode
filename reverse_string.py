def reverseString(s: list[str]) -> list[str]:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        s[i], s[-i-1] = s[-i-1], s[i]

    return s


reverseString(["h", "e", "l", "l", "o"])  #?
reverseString(["H","a","n","n","a","h"]) #?