from choices import get_user_choice, get_comp_choice
from winer import determine_winner


class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.comp_score = 0

    def play(self):
        print("Welcome to Rock-Paper-Scissors! Type 'q' to quit.")
        while True:
            user_choice = get_user_choice()
            if user_choice == "q":
                break
            comp_choice = get_comp_choice()
            print(f"Computer chose: {comp_choice}")
            result = determine_winner(user_choice, comp_choice)
            if result == "win":
                self.user_score += 1
                print("You Won!")
            elif result == "lose":
                self.comp_score += 1
                print("You Lost!")
            else:
                print("It's a Draw!")
            print(f"Scores -> You: {self.user_score}, Computer: {self.comp_score}")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
