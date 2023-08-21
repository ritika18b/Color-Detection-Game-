# Color-Detection-Game-

# import the modules
import tkinter
import random

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0

timeleft = 30

def save():
        f=open("score.txt" ,"a")
        f.write(str (name.get()) +"     "+ str (score) + "\n")
        f.close()

def leaderboard(event):
        lb =tkinter.Tk()
        lb.geometry("300x300")
        f=open("score.txt" ,"r+")
        tkinter.Label(lb ,text="Name"+"   "+"Score",font = ('Arialblack', 12)).pack(side="top")
        tkinter.Label(lb ,text= f.read()).pack()
        f.close()
        lb.mainloop()
        

# function that will start the game.
def startGame(event):
    
    if timeleft == 30:
        
        # start the countdown timer.
        countdown()
        
    # run the function to  choose the next colour.
    nextColour()

# Function to choose and
# display the next colour.
def nextColour():

    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
            
            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)
        
        random.shuffle(colours)
        
        # change the colour to type, by changing the
        # text and the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))
        
        # update the score.
        scoreLabel.config(text = "Score: " + str(score))


# Countdown timer function
def countdown():

    global timeleft
    global name

    # if a game is in play
    if timeleft > 0:

        # decrement the timer.
        timeleft -= 1
        
        # update the time left label
        timeLabel.config(text = "Time left: "+ str(timeleft))
                                
        # run the function again after 1 second.
        timeLabel.after(1000, countdown)

    else:
        tkinter.Label(text = "You  loose",font = ('Helvetica', 12)).pack()
        e.config(state="disabled")
        name = tkinter.Entry()
        tkinter.Label( text="Enter your name",font = ('Helvetica', 12)).pack()
        name.pack()
        tkinter.Button(text="Submit",command=save).pack()
        
# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the size
root.geometry("400x500")

# add an instructions label
instructions = tkinter.Label(root, text = " Detect The Colour ,Write The Colour Name",font = ('Arial Black', 12))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Helvetica', 12))
                
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
root.bind("<space>" , leaderboard)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
