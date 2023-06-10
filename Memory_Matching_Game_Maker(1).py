"""
Memory matching game
->by Game Maker
"""
#import needed modules and Libraries
import tkinter as tk
import random
import time

base = tk.Tk()  # create new Tkinter window
base.title("Memory Matching Game")  # set the title of the window
base.resizable(width=False, height=False)  # unable the user to change the size of the window
base['background'] = '#D6E4ED'  # set background color using the color code

# add greeting text to the user as (Tkinter Label)
label = tk.Label(base, text="Hello, Let's play *Memory Matching Game*!", font=('Impact', 25), fg='#000000',
                 bg='#97C6DC')
label.pack(padx=20, pady=20)

#this code section is for the easy level, the button command leads to the function of the game
easy_Button = tk.Button(command=lambda: game_start_easy(), text="EASY", font=("Times New Roman", 20),
                        fg='black', bg='#A63CFF', width=9,height=2)
easy_Button.pack(padx=30, pady=30)
#this code section is for the medium level, the button command leads to the function of the game
medium_Button = tk.Button(command=lambda: game_start_medium(), text="MEDIUM", font=("Times New Roman", 20),
                        fg='black', bg='#37DD4B', width=9,height=2)
medium_Button.pack(padx=30, pady=30)
#this code section is for the hard level, the button command leads to the function of the game
hard_Button = tk.Button(command=lambda: game_start_hard(), text="HARD", font=("Times New Roman", 20),
                        fg='black', bg='#FA3F5E', width=9,height=2)
hard_Button.pack(padx=30, pady=30)
    
moves = 0  #set moves to 0
pairs = 0  #set pairs to 0

def game_start_easy():   #define the function of easy level
    user_name = tk.simpledialog.askstring("Welcome","Tell us your beautiful name:") #get the user name as a simpledialog
    base.destroy()  # Destroy the initial(greeting+levels) window
    game_window = tk.Tk()  # create new Tkinter window for the game
    game_window.title("Memory Matching Game")  # set the title of the window
    game_window.resizable(width=False, height=False)  # unable the user to change the size of the window

    buttons = {}  #this is to store the buttons in
    first = True  #to check if the symbol button is the first in the match
    #to track the last button pressed by the user
    lastx = 0  
    lasty = 0

    buttonSymbols = {}  #this is to store the symbols of the buttons in
    symbols = ['✨', '✨', '🧪', '🧪',    #symbols list for easy level
               '🐦', '🐦', '💜', '💜',
                '🦋', '🦋', '🌟', '🌟']
               
    random.shuffle(symbols)  #this to mix up the symbols in the list (from random library)

    for x in range(4):       # create nested loop
        for y in range(3):   ##
            button = tk.Button(game_window, command=lambda x=x, y=y: show_symbol(x, y), width=8, height=4,
              text="⏹️", font=('Arial', 20), fg='#5A3479', bg='#ECD9FC') #this create the symbols buttons with the written format
            button.grid(column=x, row=y)  #sets the button location in the grid window
            buttons[x, y] = button  #this saves each button in the created (buttons) dicitionary
            buttonSymbols[x, y] = symbols.pop() ##to set the buttons symbol
            
    def show_symbol(x, y):  #define show_symbol function
        global moves, pairs  #make moves and pairs variables global
        nonlocal first, lastx, lasty  
        #these to show the symbols
        buttons[x, y]['text'] = buttonSymbols[x, y]  
        buttons[x, y].update_idletasks()

        if first:  #if its the first turn
        #these detect the last pressed button
            lastx = x   
            lasty = y
            first = False
            moves += 1  #add 1 to moves
        elif lastx != x or lasty != y:  #so the user don't cheat by clicking the button twice
            if buttons[lastx, lasty]['text'] != buttons[x, y]['text']: #this section for the unmatched symbols
                time.sleep(0.5)  #the time until the symbols are hidden again
                buttons[lastx, lasty]['text'] = '⏹️'  ##hidesymbol
                buttons[x, y]['text'] = '⏹️' ##hide symbol
            else:  #disable the button if matched
                buttons[lastx, lasty]['command'] = tk.DISABLED   #disable the button after matching
                buttons[x, y]['command'] = tk.DISABLED  #disable the matched button
                pairs += 1  #add 1 to pairs
                if pairs == len(buttons)/2:  #checks the number of pairs(if the user won)
                    tk.messagebox.showinfo("Congratulations!","WOW, You did it " + user_name + " ! in " +str(moves) +" moves") #show a massagebox
                    game_window.destroy()  #destroy game_window                                                                #for the user 
                    base.destroy()   #destroy base window
            first = True
            
    game_window.mainloop()  #loop 

def game_start_medium():   #**same format as the game_start_easy just the number of symbols is changed
    user_name = tk.simpledialog.askstring("Welcome","Tell us your beautiful name:")
    base.destroy()  # Destroy the initial window
    game_window = tk.Tk()  # create new Tkinter window for the game
    game_window.title("Memory Matching Game")  # set the title of the window
    game_window.resizable(width=False, height=False)  # unable the user to change the size

    buttons = {}
    first = True
    lastx = 0
    lasty = 0

    buttonSymbols = {}
    symbols = ['✨', '✨', '🧪', '🧪', '🖼', '🖼',
               '👑', '👑', '🐦', '🐦', '💜', '💜',
               '🔥', '🔥', '🦋', '🦋', '🌟', '🌟']
               
    random.shuffle(symbols)

    for x in range(6):
        for y in range(3):
            button = tk.Button(game_window, command=lambda x=x, y=y: show_symbol(x, y), width=8, height=4,
                               text="⏹️", font=('Arial', 20), fg='#297B33', bg='#DBF5DE')
            button.grid(column=x, row=y)
            buttons[x, y] = button
            buttonSymbols[x, y] = symbols.pop()
            
    def show_symbol(x, y):
        global moves, pairs
        nonlocal first, lastx, lasty  
        buttons[x, y]['text'] = buttonSymbols[x, y]
        buttons[x, y].update_idletasks()

        if first:
            lastx = x
            lasty = y
            first = False
            moves += 1
        elif lastx != x or lasty != y:
            if buttons[lastx, lasty]['text'] != buttons[x, y]['text']:
                time.sleep(0.5)
                buttons[lastx, lasty]['text'] = '⏹️'
                buttons[x, y]['text'] = '⏹️'
            else:
                buttons[lastx, lasty]['command'] = tk.DISABLED
                buttons[x, y]['command'] = tk.DISABLED
                pairs += 1
                if pairs == len(buttons)/2:
                    tk.messagebox.showinfo("Congratulations!","WOW, You did it " + user_name + " ! in " +str(moves) +" moves")
                    game_window.destroy()
                    base.destroy()
            first = True
            
    game_window.mainloop()
    
def game_start_hard():  #**same format as the game_start_easy just the number of symbols is changed
    user_name = tk.simpledialog.askstring("Welcome","Tell us your beautiful name:")
    base.destroy()  # Destroy the initial window
    game_window = tk.Tk()  # create new Tkinter window for the game
    game_window.title("Memory Matching Game")  # set the title of the window
    game_window.resizable(width=False, height=False)  # unable the user to change the size

    buttons = {}
    first = True
    lastx = 0
    lasty = 0

    buttonSymbols = {}
    symbols = ['🔪', '🔪', '🔫', '🔫', '💣', '💣','🕷','🕷',
               '✨', '✨', '🧪', '🧪', '🖼', '🖼','♠','♠',
               '👑', '👑', '🐦', '🐦', '💜', '💜','♣','♣',
               '🔥', '🔥', '🦋', '🦋', '🌟', '🌟','💡','💡']
    random.shuffle(symbols)

    for x in range(8):
        for y in range(4):
            button = tk.Button(game_window, command=lambda x=x, y=y: show_symbol(x, y), width=8, height=4,
                               text="⏹️", font=('Arial', 20), fg='#8C072F', bg='#F9D5E0')
            button.grid(column=x, row=y)
            buttons[x, y] = button
            buttonSymbols[x, y] = symbols.pop()
            
    def show_symbol(x, y):
        global moves, pairs
        nonlocal first, lastx, lasty  
        buttons[x, y]['text'] = buttonSymbols[x, y]
        buttons[x, y].update_idletasks()

        if first:
            lastx = x
            lasty = y
            first = False
            moves += 1
        elif lastx != x or lasty != y:
            if buttons[lastx, lasty]['text'] != buttons[x, y]['text']:
                time.sleep(0.5)
                buttons[lastx, lasty]['text'] = '⏹️'
                buttons[x, y]['text'] = '⏹️'
            else:
                buttons[lastx, lasty]['command'] = tk.DISABLED
                buttons[x, y]['command'] = tk.DISABLED
                pairs += 1
                if pairs == len(buttons)/2:
                    tk.messagebox.showinfo("Congratulations!","WOW,You did it " + user_name + " ! in " +str(moves) +" moves")
                    game_window.destroy()
                    base.destroy()
            first = True
            
    game_window.mainloop()    
    
base.mainloop()


