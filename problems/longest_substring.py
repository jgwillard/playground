class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = ''
        longest_substring = 0
        for char in s:
            if char in current_substring:
                length_of_substring = len(current_substring)
                # if the char is in the current substring, find the
                # location of its occurrence (there will only be one)
                # and take all chars after that location as the new
                # substring and then append char
                occurrence = current_substring.find(char)
                current_substring = current_substring[occurrence+1:]
                current_substring += char
                if length_of_substring > longest_substring:
                    # if the current substring is longer than the
                    # previous longest, replace it
                    longest_substring = length_of_substring
            else:
                current_substring += char

        length_of_substring = len(current_substring)
        if length_of_substring > longest_substring:
            longest_substring = length_of_substring

        return longest_substring
