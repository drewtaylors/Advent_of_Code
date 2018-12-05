from __future__ import print_function

list_of_freqs = []

with open('input.txt', 'rb') as f:
    for line in f:
        list_of_freqs.append(int(line.strip()))

# part a
def total_sum(frequencies):
    total = 0
    for freq in frequencies:
        total += freq
    return total

# part b
def check_for_sum(frequencies):
    total = 0
    sum_frequencies = [0]
    while True:
        for freq in frequencies:
            total += freq
            if total not in sum_frequencies:
                sum_frequencies.append(total)
            else:
                return total

print(total_sum(list_of_freqs))
print(check_for_sum(list_of_freqs))
