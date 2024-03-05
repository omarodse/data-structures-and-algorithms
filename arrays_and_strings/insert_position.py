
def searchInsert(nums, target) -> int:

    """
        Approach: Use binary search to find the insert position for the target. The search narrows the possible location to either a found target or the next larger element's position.
        Thought Process: Given the sorted nature of the array, binary search is an optimal strategy to minimize the number of comparisons. If the target is found, return its index. If not, the loop terminates when 'low' is at the insert position for the target (the point where all elements to the left are smaller, and all to the right are larger).
        Time Complexity: O(log n), where n is the number of elements in the array. Binary search cuts the search space in half with each iteration.
        Space Complexity: O(1), as the search is done in place using pointers, requiring no additional storage proportional to the input size.
        
        :param nums: a sorted array of integers.
        :param target: the target value to search for.
        :return: The index if the target is found; otherwise, the index where it would be if it were inserted in order.
    """

    low = 0
    high = len(nums) -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

#tests
if __name__ == "__main__":
    test_cases = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([1,3,5,6], 0, 0),
        ([1], 0, 0),
    ]
    
    for nums, target, expected in test_cases:
        result = searchInsert(nums, target)
        print(f"nums: {nums}, target: {target} => Insert position: {result} (Expected: {expected})")


#conclusion 
"""
In wrapping up this 'Search Insert Position' challenge, we can see the power of binary search. Instead of checking every single element, 
it cleverly cuts down the possibilities each time, which speeds things up, especially with big lists. 
What struck me the most was not just finding if a number is in the list, but also figuring out where to slot in a new number if it isn't there already. 
It was a cool reminder that sometimes, the smartest way to solve a problem isn't the most straightforward one but thinking a bit differently can lead to better solutions.
"""