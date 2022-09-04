from typing import List


def binary_search(ls: List[int], target: int) -> int:
    """
    Returns the index of first list where element is larger than target
    """
    start = 0
    end = len(ls) - 1
    mid = (start + end) // 2
    while end - start > 1:
        print(start, mid, end)
        if ls[mid] > target:  # search in left part
            end = mid
        elif ls[mid] < target:  # search in right part
            start = mid
        else:
            return mid
        mid = (start + end) // 2
    print(f"Ends at {start}, {mid}, {end}")
    return start if ls[start] > target else end


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
