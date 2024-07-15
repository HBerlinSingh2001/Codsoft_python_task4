
#Rock-Paper-Scissors Game

import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.configure(bg='black')
        self.root.geometry("500x300")  # Set window size

        self.user_score = 0
        self.computer_score = 0

        # Create frames for better layout management
        self.top_frame = tk.Frame(root, bg='black')
        self.top_frame.pack(pady=10)

        self.middle_frame = tk.Frame(root, bg='black')
        self.middle_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(root, bg='black')
        self.bottom_frame.pack(pady=10)

        self.user_choice_label = tk.Label(self.top_frame, text="Your Choice: ", font=('Helvetica', 14), fg='white', bg='black')
        self.user_choice_label.pack(side=tk.LEFT, padx=10)

        self.computer_choice_label = tk.Label(self.top_frame, text="Computer's Choice: ", font=('Helvetica', 14), fg='white', bg='black')
        self.computer_choice_label.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.middle_frame, text="Result: ", font=('Helvetica', 14), fg='white', bg='black')
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.middle_frame, text="Score: You 0 - 0 Computer", font=('Helvetica', 14), fg='white', bg='black')
        self.score_label.pack(pady=10)

        button_font = ('Helvetica', 12)

        # Function to create a button with a shadow effect
        def create_shadow_button(frame, text, command):
            shadow = tk.Frame(frame, bg='gray', bd=1)
            button = tk.Button(shadow, text=text, font=button_font, bg='orange', command=command, relief='flat')
            shadow.pack(side=tk.LEFT, padx=20, pady=10)
            button.pack(padx=5, pady=5)
            return button

        self.rock_button = create_shadow_button(self.bottom_frame, "Rock", lambda: self.play_game('rock'))
        self.paper_button = create_shadow_button(self.bottom_frame, "Paper", lambda: self.play_game('paper'))
        self.scissors_button = create_shadow_button(self.bottom_frame, "Scissors", lambda: self.play_game('scissors'))
        self.reset_button = create_shadow_button(self.bottom_frame, "Reset", self.reset_game)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.get_winner(user_choice, computer_choice)

        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

        if winner == 'tie':
            self.result_label.config(text="Result: It's a tie!")
        elif winner == 'user':
            self.result_label.config(text="Result: You win!")
            self.user_score += 1
        else:
            self.result_label.config(text="Result: You lose!")
            self.computer_score += 1

        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_choice_label.config(text="Your Choice: ")
        self.computer_choice_label.config(text="Computer's Choice: ")
        self.result_label.config(text="Result: ")
        self.score_label.config(text="Score: You 0 - 0 Computer")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
