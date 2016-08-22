from tkinter import*
 
root = Tk() #defines a new window
root.geometry("200x200") #sets size of the window
root.title('Guess the Number') #title of window
frame1 = Frame(root).grid(row = 0, column = 0) #creates frame
 
 
 
import random
import math
 
# initialize global variables used in your code
comp_number = 0
guesses = 0
 
# define event handlers for control panel
 
def reset():
    rand_game = random.randrange(0,2)
    print ("")
    print ("NEW GAME!")
    if rand_game == 0:
        range100()
    else:
        range1000()
    print ("")
    
    
def range100():
    # button that changes range to range [0,100) and restarts
    global comp_number, guesses
    comp_number = random.randrange(0,100)
    guesses = 7
    print ("The range is 0 - 100")
    print ("The number of guesses remaining: "), guesses
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global comp_number, guesses
    comp_number = random.randrange(0,1000)
    guesses = 10
    print ("The range is 0 - 1000")
    print ("The number of guesses remaining: "), guesses
    
    
    
def get_input(guess):
    global comp_number, guesses
    guess = entry_box.get()
    entry_box.delete(0,END)   # this is optional but clears the text box when you hit return
    my_guess = int(guess)
    guesses -= 1
    print ("Guess was "), my_guess
    print ("Number of guesses remaining: "), guesses
    if guesses < 0:
        print ("You lose! The number was "), comp_number
        reset()
    elif comp_number < my_guess:
        print ("Guess lower!")
    elif comp_number > my_guess:
        print ("Guess higher!")
    else: #number == my_guess:
        print ("You guessed it! The number is "), comp_number
        reset()
    print ("")
 
    
 
 
 
# register event handlers for control elements
 
b_r = Button(frame1, text= 'Range is [0, 99)', command=range100, width = 20, pady =2).grid(row =0, column =0)
b_r1000 = Button(frame1, text='Range is [0,999)', command=range1000, width = 20,pady = 2).grid(row = 1, column = 0)
L1 = Label(frame1, text="Enter a guess:").grid(column = 0, row = 3, padx = 2, pady = 6)
entry_box = Entry(frame1, width=12)
entry_box.grid(row=4, column = 0, padx = 2, pady = 2)
entry_box.bind('<Return>', get_input)
 
#start tkinter
mainloop()
