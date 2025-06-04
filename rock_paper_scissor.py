import tkinter as tk
import random

# Game logic
choices = ["Rock", "Paper", "Scissor"]
user_score = 0
comp_score = 0

def determine_winner(user, comp):
    if user == comp:
        return "Tie"
    elif (user == "Rock" and comp == "Scissor") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissor" and comp == "Paper"):
        return "User"
    else:
        return "Computer"

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    winner = determine_winner(user_choice, comp_choice)
    result_text = f"User: {user_choice} | Computer: {comp_choice}\n"
    if winner == "Tie":
        result_text += "Result: It's a Tie!"
    elif winner == "User":
        user_score += 1
        result_text += "Result: You Win!"
    else:
        comp_score += 1
        result_text += "Result: Computer Wins!"
    result_label.config(text=result_text)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# UI setup
root = tk.Tk()
root.title("Rock Paper Scissor")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

result_label = tk.Label(frame, text="Make your choice!", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(frame, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

btn_frame = tk.Frame(frame)
btn_frame.pack(pady=10)

for choice in choices:
    tk.Button(btn_frame, text=choice, width=10, font=("Arial", 12),
              command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Play Again (Reset Score)", font=("Arial", 10), command=reset_game).pack(pady=10)

root.mainloop()