from random import choice
import csv

battle_table = []


def read_rolls(table):
    with open(table) as bt:
        reader = csv.reader(bt)
        for row in reader:
            battle_table.append(row)


class Player():
    def __init__(self, name):
        self.name = name


class Rolls():
    def __init__(self, name, beats, beaten_by):
        self.name = name
        self.beats = beats
        self.beaten_by = beaten_by

    def can_defeat(self, opponent):
        if opponent.name == self.name:
            return 'draws against'
        elif opponent.name in self.beaten_by:
            return 'is beaten by'
        elif opponent.name in self.beats:
            return 'beats'


def print_line(n):
    print(n*'-')


def print_header():
    print('---------------------------------')
    print('         Jan Ken Pon')
    print('---------------------------------')
    print()


def get_players_name():
    name = input("Enter your name: ")
    return name

def get_players_roll(rolls):
    choices = {}
    for i, roll in enumerate(rolls):
        choices[i+1] = roll
        print(f"{i+1} {roll.name}")
    players_choice = input("Enter your throw: ")
    return choices[int(players_choice)]


def build_the_three_rolls(which_game):
    rolls = []
    if which_game == 'b':
        read_rolls('battle-table.csv')
    else:
        read_rolls('jkp.csv')

    def battle(wol):
        return [battle_table[0][i] for i, x in enumerate(roll) if x == wol]

    for roll in battle_table[1:]:
        rolls.append(Rolls(name=roll[0], beats=battle('win'), beaten_by=battle('lose')))
    return rolls


def game_loop(player1, player2, rolls):
    for count in range(1,4):
        p2_roll = choice(rolls)
        p1_roll = get_players_roll(rolls)
        outcome = p1_roll.can_defeat(p2_roll)
        outcome_line = f"Round {count}: {player1.name}'s {p1_roll.name} {outcome} {player2.name}'s {p2_roll.name}"
        print_line(len(outcome_line))
        print(outcome_line)
        print_line(len(outcome_line))

def main():
    print_header()
    game =  input('Do you want to go [b]ig? ')
    rolls = build_the_three_rolls(game)
    name = get_players_name()

    player1 = Player(name)
    player2 = Player("The Computer")

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()
