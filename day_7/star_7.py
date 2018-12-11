from __future__ import print_function
import re

class Kahn:

    def __init__(self, rules):
        # parse rules into instructions
        self.instructions = dict()
        for rule in rules:
            first_instruct = rule[0]
            second_instruct = rule[1]
            if first_instruct not in self.instructions:
                self.instructions[first_instruct] = {
                    'dependency': [],
                    'degree': 0
                }
            if second_instruct not in self.instructions:
                self.instructions[second_instruct] = {
                    'dependency': [],
                    'degree': 0
                }
            self.instructions[first_instruct]['dependency'].append(second_instruct)
            self.instructions[second_instruct]['degree'] += 1

        # intiialize queue
        self.queue = []
        for instruction in self.instructions:
            self.instructions[instruction]['dependency'].sort()
            if self.instructions[instruction]['degree'] == 0:
                self.queue.append(instruction)


        # create organized instruction strings
        self.order = ''

        while self.queue:
            self.queue.sort()
            self.order += self.queue[0]
            self.read_dependencies(self.instructions[self.queue[0]])
            self.queue.pop(0)

    def read_dependencies(self, instruction):
        for dependent in instruction['dependency']:
            self.instructions[dependent]['degree'] -= 1
            if self.instructions[dependent]['degree'] == 0:
                self.queue.append(dependent)
    
if __name__ == "__main__":
    rules = []

    with open('input.txt', 'rb') as f:
        for line in f:
            rule = []
            steps = re.findall(r'[sS]tep [A-Z]', line)
            for step in steps:
                rule.append(step.split()[-1])
            rules.append(rule)

    sorter = Kahn(rules)
    print(sorter.order)
    
