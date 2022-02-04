from tkinter import *
import tkinter as tk 
import random 
colours = ['Cyan','Black','Purple','Yellow','Blue', 'Green','Light Blue','White','Orange','Brown','Red'] 
score = 0
time_left = 40 
def start_Game(event):
    if time_left == 40:
        countdown()
    next_Colour() 
def next_Colour():
    global score 
    global timeleft
    if time_left > 0:
        entry.focus_set()
        if entry.get().lower() == colours[1].lower():
            score += 1
        entry.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score)) 
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text = "Time Left: "+ str(time_left))
        timeLabel.after(1000, countdown) 
wd = tk.Tk() 
wd.title("Pythontpoint") 
wd.geometry("500x400") 
instructions = tk.Label(wd, text = "Type in the colour of the words, not the word text!",font = ('Times New Roman', 15)) 
instructions.pack() 
scoreLabel = tk.Label(wd, text = "Press Enter To Start", font = ('Times New Roman', 15)) 
scoreLabel.pack() 
timeLabel = tk.Label(wd, text = "Time left: " +str(time_left), font = ('Times New Roman', 15)) 				
timeLabel.pack() 
label = tk.Label(wd, font = ('Times New Roman', 60)) 
label.pack() 
entry = tk.Entry(wd) 
wd.bind('<Return>', start_Game) 
entry.pack() 
entry.focus_set() 
wd.mainloop() 