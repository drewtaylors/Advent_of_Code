from __future__ import print_function
import re

class CircleList:
    def __init__(self):
        self.order = [0]
        self.index = 0
        self.length = 1

    def add_marble(self, number):
        score = 0

        if number == 1:
            self.order = [0, 1]
            self.index = 1
            self.length = 2
        elif number == 2:
            self.order = [0, 2, 1]
            self.index = 1
            self.length = 3
        elif number % 23 == 0:
            self.index -= 7
            if self.index < 0:
                self.index += self.length
            self.length -= 1
            score = number + self.order.pop(self.index)
        else:
            self.index += 2
            if self.index <= self.length:
                self.order.insert(self.index, number)
            else:
                self.index -= self.length
                self.order.insert(self.index, number)
            self.length += 1

        return score
        
class Player:
    def __init__(self):
        self.score = 0

if __name__ == "__main__":

    input = []

    with open('input.txt', 'rb') as f:
        for line in f:
            rule = []
            input = [int(x) for x in re.findall(r'\d+', line)]

    num_players = input[0]
    num_marbles = input[1]
    
    circle_list = CircleList()
    players = []
    for i in range(num_players):
        players.append(Player())

    for i in range(1, num_marbles + 1):
        players[i % num_players].score += circle_list.add_marble(i)

    scores = []
    for player in players:
        scores.append(player.score)
    
    # part a
    print(max(scores))

    for i in range(num_marbles + 1, num_marbles*100 + 1):
        players[i % num_players].score += circle_list.add_marble(i)

    scores = []
    for player in players:
        scores.append(player.score)
    
    # part b
    print(max(scores))


