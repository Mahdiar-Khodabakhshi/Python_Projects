def determine_winner(user_choice, comp_choice):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if user_choice == comp_choice:
        return "draw"
    elif rules[user_choice] == comp_choice:
        return "win"
    else:
        return "lose"