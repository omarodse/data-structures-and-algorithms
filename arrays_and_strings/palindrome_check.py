"""
Palindrome Checker

This problem is inspired by a challenge on LeetCode. Visit https://leetcode.com for more details.
The solutions here are provided for educational purposes and to illustrate different problem-solving approaches.

Author: Omar Rodriguez 
"""

import string

def isPalindrome(s) -> bool:
        """
        Approach: Remove all punctuation using a translation table, convert the string to lowercase, and remove spaces. Then, check if the cleaned string is a palindrome by comparing characters from the start and end, moving towards the center.
        Thought Process: The primary goal is to normalize the string by removing non-alphanumeric characters and making it case-insensitive. Utilizing Python's string manipulation capabilities simplifies the preprocessing. The final step involves a classic two-pointer approach to compare the characters.
        Time Complexity: O(n), where n is the length of the string. The translation, case conversion, and space removal each run in linear time, and so does the final palindrome check.
        Space Complexity: Higher than O(1) due to creating a new string for the cleaned version, but generally O(n) for storing the cleaned string.
        
        :param s: String to check for palindrome properties.
        :return: True if the string is a palindrome when ignoring cases, spaces, and punctuation. False otherwise.
        """

        translation_table = str.maketrans('', '', string.punctuation)
        rem_punct = s.translate(translation_table)
        sentence = ''.join(rem_punct.lower().split())
        
        start, end = 0, len(sentence) - 1
        while start < end:
            if sentence[start] != sentence[end]:
                return False
            start += 1
            end -= 1
        return True

def isPalindrome_opt(s) -> bool:
        
        """
        Approach: Directly iterate over the original string using two pointers to compare characters from both ends, skipping non-alphanumeric characters. This method avoids creating additional strings, thereby optimizing space usage.
        Thought Process: Recognizing that the definition of a palindrome for this problem ignores non-alphanumeric characters and case, the solution skips irrelevant characters and directly compares relevant ones in a single pass. This direct approach minimizes space complexity by not requiring an additional cleaned string.
        Time Complexity: O(n), where n is the length of the string. Each character is checked at most once, with some skipped due to being non-alphanumeric.
        Space Complexity: O(1), significantly improving over the first approach by avoiding the creation of a new string and instead operating directly on the input.
        
        :param s: String to check for palindrome properties.
        :return: True if the string is a palindrome under the problem's specific conditions. False otherwise.
        """

        start, end = 0, len(s) - 1
        
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True


#Tests
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        " ",
        "a.",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?"
    ]

    print("Testing isPalindrome function:")
    for test in test_cases:
        print(f"{test!r} -> {isPalindrome(test)}")

    print("\nTesting isPalindrome_opt function:")
    for test in test_cases:
        print(f"{test!r} -> {isPalindrome_opt(test)}")


"""
General Reflection:

- Developed two approaches to solve the palindrome checker problem, highlighting a balance between readability and space efficiency.
- Initial Solution (`isPalindrome`): Utilizes Python's string methods. This approach, while straightforward and readable, incurs extra space due to the creation of a new string for the cleaned input.
- Optimized Solution (`isPalindrome_opt`): This method enhances space complexity to O(1) by avoiding additional strings.
- Key Insight: This comparison underscores the trade-off between space and time complexities and the impact of Python's string methods on space usage.
"""