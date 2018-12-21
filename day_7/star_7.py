from __future__ import print_function
import re
import numpy

class Kahn:

    def __init__(self, rules, workers):
        # parse rules into instructions
        self.instructions = dict()
        self.workers = workers
        for rule in rules:
            first_instruct = rule[0]
            second_instruct = rule[1]
            if first_instruct not in self.instructions:
                self.instructions[first_instruct] = {
                    'dependency': [],
                    'degree': 0,
                    'time': ord(first_instruct) - 4,
                }
            if second_instruct not in self.instructions:
                self.instructions[second_instruct] = {
                    'dependency': [],
                    'degree': 0,
                    'time': ord(second_instruct) - 4,
                }
            self.instructions[first_instruct]['dependency'].append(second_instruct)
            self.instructions[second_instruct]['degree'] += 1

        # intiialize queue
        self.queue = []
        for instruction in self.instructions:
            self.instructions[instruction]['dependency'].sort()
            if self.instructions[instruction]['degree'] == 0:
                self.queue.append(instruction)

        # initialize worker schedule
        self.worker_schedule = []
        self.queue.sort()

        for instruction in self.queue[:]:
            if len(self.worker_schedule) < self.workers:
                self.worker_schedule.append(instruction)
                self.queue.remove(instruction)

        # create organized instruction strings
        self.order = ''

        while self.worker_schedule:
            print(self.order)
            print(self.worker_schedule)
            print(self.queue)
            print(self.instructions)
            print('')
            self.finished_work = []

            for instruction in self.worker_schedule[:]:
                self.instructions[instruction]['time'] -= 1
                if self.instructions[instruction]['time'] == 0:
                    self.order += instruction
                    self.worker_schedule.remove(instruction)

                    # check dependencies of instructions that were finished
                    for dependent in self.instructions[instruction]['dependency']:
                        self.instructions[dependent]['degree'] -= 1
                        if (self.instructions[dependent]['degree'] == 0):
                            self.queue.append(dependent)
                            self.queue.sort()

            for instruction in self.queue[:]:
                if len(self.worker_schedule) < self.workers:
                    self.worker_schedule.append(self.queue[0])
                    self.queue.pop(0)
                    self.worker_schedule.sort()
    
# wrong answer: FHICMRYDTXBOPWAJQNVGZUEKLS

if __name__ == "__main__":
    rules = []

    with open('input.txt', 'rb') as f:
        for line in f:
            rule = []
            steps = re.findall(r'[sS]tep [A-Z]', line)
            for step in steps:
                rule.append(step.split()[-1])
            rules.append(rule)

    sorter = Kahn(rules, 5)
    print(sorter.order)
    
