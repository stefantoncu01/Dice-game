import random

MINIM = 1
MAXIM = 6

class Player:
    def __init__(self, name):
        self.name = name
        self._score = 0
        self._first = False
        self.continue_game = "yes"

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, new_value):
        self._first = new_value

    @property
    def continue_g(self):
        return self.continue_game

    @continue_g.setter
    def continue_g(self, answer):
        self.continue_game = answer

    @staticmethod
    def roll_dices():
        print("Rolling the dices...")
        print("The values are...")
        first_dice = random.randint(MINIM, MAXIM)
        second_dice = random.randint(MINIM, MAXIM)
        print(first_dice, second_dice)
        return first_dice, second_dice

class Game:
    def __init__(self):
        self.computer = Player(name="Computer")
        player_name = input("What is your name? ")
        self.human = Player(name=player_name)
        self.winning_score = int(input("Please select the winning score! "))

    @property
    def greet(self):
        print(f"Nice to meet you {self.human.name.capitalize()}!\n "
              f"Before we continue, I want to explain the game: we take turns in running the dice. \n "
              f"If any of us hits a double, they can roll the dice until the dice is not a double. \n "
              f"Each roll adds up to the score until someone reaches the winning score. \n "
              f"First one to reach the winning score will win the game. If you forfeit the game you will loose.\n "
              f"Let's start the game!")

    def determine_first_player(self):
        print("You roll the starting dice...")
        first_dice, second_dice = self.human.roll_dices()
        player_score = first_dice + second_dice
        print("Computer rolls the starting dice...")
        first_dice, second_dice = self.computer.roll_dices()
        computer_score = first_dice + second_dice
        if player_score > computer_score:
            print("You will roll first!")
            self.human._first = True
            return
        elif player_score == computer_score:
            print("We need to roll again because we had the same score!")
            self.determine_first_player()
        else:
            print("You will run second!")
            self.computer._first = True
            return

    def computer_roll(self):
        first_dice, second_dice = self.computer.roll_dices()
        self.computer._score += first_dice + second_dice
        while first_dice == second_dice:
            first_dice, second_dice = self.computer.roll_dices()
            self.computer._score += first_dice + second_dice
        print(f'Computer score is {self.computer._score}')

    def human_roll(self):
        first_dice, second_dice = self.human.roll_dices()
        self.human._score += first_dice + second_dice
        while first_dice == second_dice:
            first_dice, second_dice = self.human.roll_dices()
            self.human._score += first_dice + second_dice
        print(f'Your score is {self.human._score}')
        self.human.continue_game = input("Do you continue the game? yes or no?").lower()

    def play(self):
        self.determine_first_player()
        while True:
            if self.human.continue_game in ['n','no']:
                break
            if self.computer.score >= self.winning_score or self.human.score >= self.winning_score:
                break
            if self.computer._first:
                self.computer_roll()
                self.human_roll()
            else:
                self.human_roll()
                self.computer_roll()

        if self.computer.score > self.human.score or self.human.continue_game in ['n','no']:
            print(f'Winner is {self.computer.name}')
        else:
            print(f'Winner is {self.human.name}')


new_game = Game()
new_game.greet
new_game.play()