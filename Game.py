import tkinter as tk
import random

# create a window
window = tk.Tk()
window.title('Tic Tac Toe')
window.geometry('270x350')

player1 = 'X'
computer = 'O'
playerScore = 0
computerScore = 0
currentPlayer = player1
userInputAllowed = True
theLabel = tk.Label(window, text=' ')

# on button click
def click(b):
    global currentPlayer
    global playerScore
    global computerScore 
    global theLabel
    global userInputAllowed

    if userInputAllowed:
        if b['text'] == ' ':
            b['text'] = currentPlayer
            b['state'] = 'disabled'
            
        checkGameState()
        if theLabel['text'] == 'Draw!' or theLabel['text'] == 'You win!' or theLabel['text'] == 'You Lose!':
            return
        
        switchPlayer() 
        if currentPlayer == computer:
            userInputAllowed = False
            window.after(400,computerTurn)

def switchPlayer():
    global currentPlayer
    if currentPlayer == player1:
        currentPlayer = computer
    else:
        currentPlayer = player1

def endGame():
    global currentPlayer
    currentPlayer = player1
    b = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for i in b:
        i['state'] = 'normal'
        i['text'] = ' '
    theLabel['text'] = ' '
    restart.grid_forget()

def checkWin():
    if b1['text'] == b2['text'] == b3['text'] != ' ' or \
       b4['text'] == b5['text'] == b6['text'] != ' ' or \
       b7['text'] == b8['text'] == b9['text'] != ' ' or \
       b1['text'] == b4['text'] == b7['text'] != ' ' or \
       b2['text'] == b5['text'] == b8['text'] != ' ' or \
       b3['text'] == b6['text'] == b9['text'] != ' ' or \
       b1['text'] == b5['text'] == b9['text'] != ' ' or \
       b3['text'] == b5['text'] == b7['text'] != ' ':
        return True
    else:
        return False

def checkGameState():
    win = checkWin()
    global playerScore
    global computerScore
    global currentPlayer
    global theLabel
    global restart
    empty_buttons = [b for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9] if b['text'] == ' ']
    if win:
        if currentPlayer == player1:
            theLabel['text'] = 'You win!'
            playerScore += 1
        else:
            theLabel['text'] = 'You Lose!'
            computerScore += 1
        for b in empty_buttons:
            b['state'] = 'disabled'
        label1 = tk.Label(window, text='Player: ' + str(playerScore))
        label2 = tk.Label(window, text='Computer: ' + str(computerScore))
        label1.grid(row=3, column=0, columnspan=1)
        label2.grid(row=3, column=2, columnspan=1)
        restart.grid(row=5, column=1, columnspan=1)
        return
    
    if all([b['text'] != ' ' for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9]]):
        theLabel['text'] ='Draw!'
        restart.grid(row=5, column=1, columnspan=1)
        return

# how the computer makes a move   
def computerTurn():
    global userInputAllowed
    empty_buttons = [b for b in [b1, b2, b3, b4, b5, b6, b7, b8, b9] if b['text'] == ' ']

    # check if computer can win
    for b in empty_buttons:
        b['text'] = computer
        if checkWin():
            b['state'] = 'disabled'
            checkGameState()
            userInputAllowed = True
            return
        
        b['text'] = ' '

    # check if player can win
    for b in empty_buttons:
        b['text'] = player1
        if checkWin():
            b['text'] = computer
            b['state'] = 'disabled'
            userInputAllowed = True
            switchPlayer()
            return
        
        b['text'] = ' '

    selected_button = random.choice(empty_buttons)
    selected_button['text'] = computer
    selected_button['state'] = 'disabled'
    userInputAllowed = True
    checkGameState()
    switchPlayer()


# create 9 buttons
b1 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b1))
b1.grid(row=0, column=0)
b2 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b2))
b2.grid(row=0, column=1)
b3 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b3))
b3.grid(row=0, column=2)
b4 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b4))
b4.grid(row=1, column=0)
b5 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b5))
b5.grid(row=1, column=1)
b6 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b6))
b6.grid(row=1, column=2)
b7 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b7))
b7.grid(row=2, column=0)
b8 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b8))
b8.grid(row=2, column=1)
b9 = tk.Button(window, text=' ', font=('Arial', 20), width=5, height=2, command= lambda: click(b9))
b9.grid(row=2, column=2)
theLabel.grid(row=3, column=1, columnspan=1)
restart = tk.Button(window, text='Play Again', command= lambda: endGame())

window.mainloop()