from typing import List 
from collections import Counter 
from itertools import zip_longest

def comman_characters(string1:str , string2:str)->List:

    counter1 = Counter(string1)
    counter2 = Counter(string2)
    intersection = counter1 & counter2 # Extreamly important !!!!! Note this DOWN !!!!!!!
    result = []
    for char, count in intersection.items():
        result.extend([char] * count)
    print(result)
    return result


def longest_common_subarray_length(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    max_length = 0
    
    # Iterate through s1 to find the longest common substring in s2
    for i in range(len1):
        for j in range(len2):
            k = 0
            while i + k < len1 and j + k < len2 and s1[i + k] == s2[j + k]:
                k += 1
            max_length = max(max_length, k)
    
    return max_length

def commanChild(s1:str , s2:str)->int:
    comman_char_list = comman_characters(string1=s1 , string2=s2)
    new_s1 = []
    new_s2 = []

    if len(comman_char_list) == len(s1):
        return len(s1) - 1
    else:
        for char1 in s1:
            if char1 in comman_char_list:
                new_s1.append(char1)
        for char2 in s2:
            if char2 in comman_char_list:
                new_s2.append(char2)
        return longest_common_subarray_length(s1=new_s1 , s2=new_s2)


#Working code !!!
# def commonChild(s1, s2):
#     m, n = len(s1), len(s2)
    
#     # Initialize the current row
#     current_row = [0] * (n + 1)
    
#     # Iterate through the strings
#     for i in range(1, m + 1):
#         previous_row = current_row[:]
#         for j in range(1, n + 1):
#             if s1[i-1] == s2[j-1]:
#                 current_row[j] = previous_row[j-1] + 1
#             else:
#                 current_row[j] = max(current_row[j-1], previous_row[j])
    
#     return current_row[n]





print(commanChild(s1="SHINCHAN" , s2="NOHARAAA"))