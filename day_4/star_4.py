from __future__ import print_function
import re
import numpy

shifts = []
guards = dict()

with open('input.txt', 'rb') as f:
    for line in f:
        shifts.append(line)

shifts.sort()
print(shifts)

guard_id = 0
timecard = numpy.zeros(60)
time_asleep = 0

for shift in shifts:
    if 'Guard' in shift:
        digits = re.search(r'#\d+', shift)
        guard_id = int(digits.group()[1:])
        if guard_id in guards:
            guard = guards[guard_id]
        else:
            guards[guard_id] = {
                'timecard': numpy.zeros(60),
            }

    elif 'falls asleep' in shift:
        minutes = re.search(r':\d+', shift)
        time_asleep = int(minutes.group()[1:])
    elif 'wakes up' in shift:
        minutes = re.search(r':\d+', shift)
        time_awake = int(minutes.group()[1:])
        for i in range(time_asleep, time_awake):
            guards[guard_id]['timecard'][i] += 1

# part a
def most_minutes_asleep():
    max_guard_id = 0
    max_minutes = 0
    max_time = 0
    for i in guards:
        minutes = sum(guards[i]['timecard'])
        if max_minutes < minutes:
            max_guard_id = i
            max_minutes = minutes
            max_time = numpy.argmax(guards[i]['timecard'])
    return max_guard_id * max_time

# part b
def minute_most_often_asleep():
    max_guard_id = 0
    max_minutes = 0
    max_time = 0
    for i in guards:
        minutes = max(guards[i]['timecard'])
        if max_minutes < minutes:
            max_guard_id = i
            max_minutes = minutes
            max_time = numpy.argmax(guards[i]['timecard'])
    return max_guard_id * max_time

print(most_minutes_asleep())
print(minute_most_often_asleep())