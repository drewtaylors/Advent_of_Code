from __future__ import print_function
from string import ascii_lowercase, ascii_uppercase

sequence_a = []
sequence_b = []

with open('input.txt', 'rb') as f:
    for line in f:
        for c in line:
            sequence_a.append(ord(c))
            sequence_b.append(ord(c))

# sample input
# aAbBcdDc len = 8

# use two pointers...
# sequence = 'dabAcCaCBAcCcaDA'
# sequence = [ord(x) for x in sequence]

# part a
def full_reaction(string):
    string_len = len(string)
    left_pointer = 0
    right_pointer = 1
    head = True

    while True:
        # print(string)
        # print(left_pointer, right_pointer)

        if right_pointer >= string_len:
            break

        if string[left_pointer] + 32 == string[right_pointer] or string[left_pointer] - 32 == string[right_pointer]:
            string[left_pointer] = 0
            string[right_pointer] = 0
            if head == True:
                right_pointer += 2
                left_pointer = right_pointer - 1
            else:
                right_pointer += 1
                while string[left_pointer] == 0:
                    left_pointer -= 1
                    if left_pointer == -1:
                        right_pointer += 1
                        left_pointer = right_pointer - 1
        else:
            head = False
            right_pointer += 1
            left_pointer = right_pointer - 1

    final_string = [x for x in string if x != 0]
    return final_string

print(len(full_reaction(sequence_a)))

# part b
LOWERCASE = [ord(x) for x in ascii_lowercase]
UPPERCASE = [ord(x) for x in ascii_uppercase]
min_length = len(sequence_b)

for i, j in zip(LOWERCASE, UPPERCASE):
    decoded_polymer = [x for x in sequence_b if x != i and x != j]
    reacted_polymer = full_reaction(decoded_polymer)
    length = len(reacted_polymer)
    if length < min_length:
        min_length = length

print(min_length)



        
# [x for x in a if x != [1, 1]]

# a = ascii code 97
# A = ascii code 65

# convert entire string to ascii
# >>> ord('a')
# 97
# >>> chr(97)
# 'a'

# difference between two letters = 32, destroy both
