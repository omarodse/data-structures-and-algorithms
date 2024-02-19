# set approach
def is_unique_ds(word):
    
    """
    Approach: Utilize a set to track seen characters. This approach leverages the fact that sets in Python do not allow duplicate elements, making it efficient to check for uniqueness. 
    Thought Process: Considering the problem's constraint on character uniqueness, using a set naturally fits as it automatically handles duplicates. This approach is straightforward and efficient for strings with a length less than the character set size.
    Time Complexity: O(n), where n is the length of the word. Iterating through the string once.
    Space Complexity: O(min(c, n)), where c is the character set size (128 for ASCII).

    :param word: String to check for uniqueness.
    :return: True if all characters are unique, False otherwise.

    """
    
    # Assuming the ASCII character set, where no string can have unique characters if length > 128.
    if len(word) > 128:
        return False
    seen_chars = set()
    for c in word:
        if c in seen_chars:
            return False
        seen_chars.add(c)
    return True


# Sort Approach
def is_unique_sort(word):

    """
    Approach: Sort the word and then check adjacent characters for any duplicates. Sorting brings identical characters next to each other, simplifying the comparison.
    Thought Process: While sorting introduces additional time complexity, it eliminates the need for extra space (assuming in-place sort). This method trades off time efficiency for space efficiency, which might be beneficial in memory-constrained environments.
    Time Complexity: O(n log n), due to sorting.
    Space Complexity: O(1) or O(n), depending on the sorting implementation.

    :param word: String to check for uniqueness.
    :return: True if all characters are unique, False otherwise.

    """

    if len(word) > 128:
        return False
    
    sorted_word = sorted(word)
    for i in range(len(sorted_word) - 1):
        if sorted_word[i] == sorted_word[i + 1]:
            return False
    return True


#Brute Force Approach
def is_unique_brute(word):

    """
    Approach: Compare every character with every other character. This brute force method does not use any additional data structures.
    Thought Process: I started with this method to understand the basic problem without any optimizations. It's clear this method is not efficient for large strings but helps build a foundational understanding of the problem.
    Time Complexity: O(n^2), where n is the length of the word.
    Space Complexity: O(1), as no additional data structures are used.

    :param word: String to check for uniqueness.
    :return: True if all characters are unique, False otherwise.

    """

    if len(word) > 128:
        return False
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return False
    return True


# Test Cases
test_words = ["", "a", "abcde", "hello", "1234567890", "!@#$%^&*()_+", "aab", "  ", "unique"]

print("Testing Data Structure Approach:")
for w in test_words:
    print(f"{w}: {is_unique_ds(w)}")

print("\nTesting Sorting Approach:")
for w in test_words:
    print(f"{w}: {is_unique_sort(w)}")

print("\nTesting Brute Force Approach:")
for w in test_words:
    print(f"{w}: {is_unique_brute(w)}")


#General Reflection:
""" 
The set-based approach offers a good balance between time and space efficiency for most practical purposes. 
The sorting method could be beneficial in scenarios where space is at a premium, despite its higher time complexity. 
The brute force approach, while not efficient for large datasets, is a good educational tool for understanding the problem's fundamentals.
"""