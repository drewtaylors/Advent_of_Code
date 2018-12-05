from __future__ import print_function
import string

list_of_ids = []

with open('input.txt', 'rb') as f:
    for line in f:
        list_of_ids.append(line.strip())

# part a
def generate_checksum(list_of_ids):
    pair_ids = 0
    triplet_ids = 0
    alphabet = string.ascii_lowercase

    for id in list_of_ids:
        lexicon = dict.fromkeys(alphabet, 0)
        pair = False
        triplet = False

        # count frequencies of each letter
        for letter in id:
            lexicon[letter] += 1

        # flip values if they contain a pair or triplet
        for letter in alphabet:
            if lexicon[letter] == 2:
                pair = True
            if lexicon[letter] == 3:
                triplet = True

        # Increment number accordingly
        if pair == True:
            pair_ids += 1
        if triplet == True:
            triplet_ids += 1

    return (pair_ids * triplet_ids)

print(generate_checksum(list_of_ids))

# part b
def check_for_one_off(word_a, word_b):
    # switch
    one_off = False

    # compare each letter in word
    for a,b in zip(word_a, word_b):
        if a == b and not one_off:
            continue
        elif a != b and not one_off:
            one_off = True
            continue
        elif a == b and one_off:
            continue
        elif a != b and one_off:
            return False
    
    return True

def loop_through_ids(list_of_ids):
    for id_a in list_of_ids:
        for id_b in list_of_ids:
            if id_a != id_b:
                if check_for_one_off(id_a, id_b) == False:
                    continue
                else:
                    return [id_a, id_b]

print(loop_through_ids(list_of_ids))
