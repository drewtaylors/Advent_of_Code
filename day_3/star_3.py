from __future__ import print_function
import re
import numpy

claim_ids = dict()
mapping = numpy.zeros((1000, 1000))

with open('input.txt', 'rb') as f:
    specs = []
    for line in f:
        specs = re.findall(r'\d+', line)
        claim_ids[specs[0]] = {
            'x': int(specs[1]),
            'y': int(specs[2]),
            'width': int(specs[3]),
            'height': int(specs[4])
        }

# #2 @ 974,796: 18x19
# part a
def map_claim(mapping, claim_id):
    for i in range(claim_id['y'], claim_id['y'] + claim_id['height']):
        for j in range(claim_id['x'], claim_id['x'] + claim_id['width']):
            mapping[i][j] += 1

for i in claim_ids:
    map_claim(mapping, claim_ids[i])

total = 0
for i in range(mapping.shape[0]):
    for j in range(mapping.shape[1]):
        if mapping[i][j] > 1:
            total += 1

print(total)

# part b
def map_check(mapping, claim_id):

    for i in range(claim_id['y'], claim_id['y'] + claim_id['height']):
        for j in range(claim_id['x'], claim_id['x'] + claim_id['width']):

            if mapping[i][j] == 1:
                continue
            else:
                return False

    return True
         
for i in claim_ids:
    result = map_check(mapping, claim_ids[i])
    if result == True:
        print(i)

# >>> a[0][1] = 1
# >>> a
# array([[0., 1., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0.]])

# >>> a.shape
# (6, 5)

# #123 @ 3,2: 5x4
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
