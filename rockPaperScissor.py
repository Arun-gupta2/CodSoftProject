import random
import tkinter as tk
from tkinter import *

object_list = ['rock', 'paper', 'scissor']

player_score = 0
computer_score = 0

def play_game(player_choice):
    global player_score, computer_score
    
    computer_choice = random.choice(object_list)
    result = ''

    if player_choice == computer_choice:
        result = "It's a draw"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissor') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissor' and computer_choice == 'paper')
    ):
        result = "Player wins"
        player_score += 1
    else:
        result = "Computer wins"
        computer_score += 1

    l2.config(text=player_choice)
    l4.config(text=computer_choice)
    l1.config(text=result)
    
    update_scores()

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    

    l2.config(text="Player")
    l4.config(text="Computer")
    l1.config(text="")
    update_scores()

def update_scores():
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")

guiWindow = tk.Tk()
guiWindow.title("rock paper scissor game")

Label(
    guiWindow,
    text="ROCK PAPER SCISSOR",
    font="normal 25 bold "
).pack(pady=20)

frame = Frame(guiWindow)
frame.pack()

Label(
    frame,
    text="Click your option",
    font="normal 15"
).pack(pady=20)

choices = ['rock', 'paper', 'scissor']
for choice in choices:
    choice=Button(
        frame,
        text=choice,
        fg="black",
        command=lambda 
        c=choice:play_game(c),
        width=20,
        font=10
    ).pack(side=LEFT, padx=15)

frame1 = Frame(guiWindow)
frame1.pack()

l2 = Label(
    frame1,
    text="Player",
    font="normal 15",
    fg='red'
)
l2.pack(side=LEFT, padx=30, pady=30)

Label(
    frame1,
    text="Vs",
    font="normal 15"
).pack(side=LEFT, padx=30, pady=30)

l4 = Label(
    frame1,
    text="Computer",
    font="normal 15",
    fg="blue"
)
l4.pack(padx=30, pady=30)

frame2 = Frame(guiWindow)
frame2.pack()

l1 = Label(
    frame2,
    text="",
    font="normal 13"
)
l1.pack(pady=10)

reset = Button(
    frame2,
    text="Reset",
    fg="green",
    command=reset_game,
    width=12,
    height=2
)
reset.pack(pady=10)

score_label = Label(
    guiWindow,
    text="Player: 0 | Computer: 0",
    font="normal 15"
)
score_label.pack(pady=10)



guiWindow.mainloop()
