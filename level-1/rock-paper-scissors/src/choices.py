import random


def get_comp_choice():
    choices = {0: "rock", 1: "paper", 2: "scissors"}
    comp_choice = random.randint(0, 2)
    return choices[comp_choice]


def get_user_choice():
    choices = {0: "rock", 1: "paper", 2: "scissors"}
    while True:
        user_input = input("Enter your choice (0: rock, 1: paper, 2: scissors, 'q' to quit): ").strip()
        if user_input == "q":
            return "q"
        if user_input.isdigit() and int(user_input) in choices:
            return choices[int(user_input)]
        print("Invalid choice. Please try again.")