def search(nums: list[int], target: int) -> int:
    start: int = 0
    end: int = len(nums) - 1

    def find(start: int, end: int) -> int | None:

        if start == end:
            return start if nums[start] == target else None
        
        mid: int = (start + end) // 2
        if nums[mid] == target:
            return mid

        return find(mid+1, end) if target > nums[mid] else find(start, mid)

    found_index = find(start, end)

    return -1 if found_index is None else found_index
    

idx = search([-1,0,3,5,9,12], 9)
print(idx)