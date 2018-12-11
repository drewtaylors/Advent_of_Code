from __future__ import print_function
import re
import numpy

def fill_matrix(matrix, coords):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            min_distance = pow(len(matrix), 2)
            min_coord_index = -1
            duplicate = False
            for i in range(len(coords)):
                distance = manhattan_distance([x,y], coords[i])
                if distance < min_distance:
                    min_distance = distance
                    min_coord_index = i
                    duplicate = False
                elif distance == min_distance:
                    if duplicate == False:
                        duplicate = True
            if duplicate == False:
                matrix[y][x] = min_coord_index
            else:
                matrix[y][x] = -1

def manhattan_distance(coord_1, coord_2):
    x_distance = abs(coord_2[0] - coord_1[0])
    y_distance = abs(coord_2[1] - coord_1[1])
    return x_distance + y_distance

def border_check(matrix):
    indexes = set()
    for coord in matrix[0]:
        indexes.add(coord)
    for coord in matrix[-1]:
        indexes.add(coord)
    for row in matrix:
        indexes.add(row[0])
        indexes.add(row[-1])
    return indexes

def find_max_area(coord_areas, infinite_coords):
    max_area = 0
    max_index = 0
    for i in range(len(coord_areas)):
        if i not in infinite_coords:
            area = coord_areas[i]
            if max_area < area:
                max_area = area
                max_index = i
    return max_index
    
def determine_valid_coords(matrix, coords):
    total_area = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            total_distance = 0
            for i in range(len(coords)):
                total_distance += manhattan_distance([x,y], coords[i])
            if total_distance < 10000:
                print('here')
                matrix[y][x] = 1
                total_area += 1
            else:
                matrix[y][x] = -1
    return total_area

if __name__ == "__main__":

    SIZE = 1000
    coords = []
    matrix = numpy.zeros((SIZE, SIZE))

    with open('input.txt', 'rb') as f:
        for line in f:
            coord = map(int, re.findall(r'\d+', line))
            coord[0] += SIZE/2
            coord[1] += SIZE/2
            coords.append(coord)

    # part a
    fill_matrix(matrix, coords)
    infinite_coords = border_check(matrix)
    coord_areas = numpy.zeros(len(coords))

    for row in matrix:
        for i in row:
            if i != -1:
                coord_areas[int(i)] += 1

    index = find_max_area(coord_areas, infinite_coords)
    print(coord_areas[index])


    print(coords)
    # part b
    matrix = numpy.zeros((SIZE, SIZE))
    print(determine_valid_coords(matrix, coords))
