from __future__ import print_function
import re

if __name__ == "__main__":
    rules = []

    with open('input.txt', 'rb') as f:
        for line in f:
            rule = []
            steps = re.findall(r'[sS]tep [A-Z]', line)
            for step in steps:
                rule.append(step.split()[-1])
            rules.append(rule)

    print(rules)

    instructions = dict()


    for rule in rules:
        first_instruct = rule[0]
        second_instruct = rule[1]
        lexicon

    
    print(queue)
