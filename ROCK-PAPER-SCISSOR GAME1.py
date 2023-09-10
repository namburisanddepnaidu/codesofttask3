import tkinter as tk
import random

def play(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()

user_choice_var = tk.StringVar()
user_choice_radio_buttons = [
    tk.Radiobutton(root, text="Rock", variable=user_choice_var, value="rock"),
    tk.Radiobutton(root, text="Paper", variable=user_choice_var, value="paper"),
    tk.Radiobutton(root, text="Scissors", variable=user_choice_var, value="scissors"),
]

for radio_button in user_choice_radio_buttons:
    radio_button.pack()

play_button = tk.Button(root, text="Play", command=lambda: play(user_choice_var.get()))
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=lambda: result_label.config(text=""))
play_again_button.pack()

root.mainloop()
