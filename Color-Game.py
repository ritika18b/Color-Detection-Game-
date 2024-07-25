import tkinter as tk
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30

def removeGameOver():
    gameOverLabel.pack_forget()
    nameLabel.pack_forget()
    name_entry.pack_forget()
    submitButton.pack_forget()
    leaderboard_instructions.pack_forget()

def restartGame():
    global score, timeleft
    score = 0
    timeleft = 30
    scoreLabel.config(text="Press enter to start")
    timeLabel.config(text="Time left: " + str(timeleft))
    label.config(text="")
    e.config(state="normal")
    e.delete(0, tk.END)
    e.focus_set()
    removeGameOver()  # Call removeGameOver() to remove game over widgets

def save():
    with open("score.txt", "a") as f:
        f.write(f"{name_entry.get()}     {score}\n")
    restartGame()

def leaderboard(event):
    lb = tk.Toplevel(root)
    lb.geometry("300x300")
    with open("score.txt", "r") as f:
        tk.Label(lb, text="Name       Score", font=('Arial Black', 12)).pack(side="top")
        tk.Label(lb, text=f.read(), font=('Helvetica', 10)).pack()
    lb.mainloop()

def startGame(event):
    global timeleft
    if timeleft == 30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        gameOver()

def gameOver():
    e.config(state="disabled")
    global gameOverLabel, nameLabel, name_entry, submitButton
    gameOverLabel = tk.Label(root, text="You Lose!", font=('Helvetica', 12), fg='red')
    gameOverLabel.pack()
    nameLabel = tk.Label(root, text="Enter your name:", font=('Helvetica', 12))
    nameLabel.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()
    submitButton = tk.Button(root, text="Submit", command=save)
    submitButton.pack()
    # Add instructions label for leaderboard
    global leaderboard_instructions
    leaderboard_instructions = tk.Label(root, text="Press Spacebar to view Leaderboard", font=('Helvetica', 12))
    leaderboard_instructions.pack(pady=5)

# Create a GUI window
root = tk.Tk()
root.title("COLORGAME")
root.geometry("400x500")

# Add instructions label
instructions = tk.Label(root, text="Detect The Colour, Write The Colour Name", font=('Arial Black', 12))
instructions.pack(pady=10)

# Add score label
scoreLabel = tk.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack(pady=10)

# Add time left label
timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack(pady=10)

# Add a label for displaying the colours
label = tk.Label(root, font=('Helvetica', 60))
label.pack(pady=20)

# Add a text entry box for typing in colours
e = tk.Entry(root, font=('Helvetica', 14))
e.pack(pady=10)

# Bind the startGame function to the Enter key
root.bind('<Return>', startGame)
root.bind("<space>", leaderboard)

e.focus_set()

# Start the GUI
root.mainloop()
