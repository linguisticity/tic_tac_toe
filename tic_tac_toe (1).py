'''
*****************************************************************************************
*
*        		=================================================
*           	e-Yantra School Robotics Competition (eYSRC 2023)
*        		=================================================
*
*  This script is to be used to implement Mini Assignment titled- 'Tic Tac Toe: Player vs Player'.
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*  
*  e-Yantra - A MOE project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          
# 					[ Team-ID ]
# Author List:      
# 					[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         tic_tac_toe.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################
import turtle
import threading
from sheet_dot_best_manager import sheet_manager
##############################################################

connect=sheet_manager('https://sheet.best/api/sheets/49dbdd14-2dce-4a70-be43-7adcad372027')
connected=False
playing_as=''
data=[]
# Initialize the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Tic Tac Toe")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('light gray')
screen.tracer(0, 0)
turtle.hideturtle()
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def atoi(a, b):
    if a == 'o' and b == False:
        return 2
    elif a == 'o' and b == True:
        return 1
    elif a=='x' and b==False:
        return 1
    elif a=='x' and b==True:
        return 2
    return 1



def clear():
    n=len(data)
    print(n, 'clear() called')
    for i in range(2, n+2):
        connect.delete_data(i)

def get_turn():
    if data!=None and data!=[]:
        turno=data[0]['turn']
        if turno==None:
            set_turn('x')
            return 'x'
        return turno
    else:
        set_turn('x')
    return 'x'

def set_turn(t):
    global turn
    connect.update_fields(2,{'turn':t})
    turn=t


def set_player(x,y):
    connect.update_fields(2,{x: y})
        
    
    
def inito(x,y):
    print('inito called')
    global data
    global connected
    global playing_as
    
    print(data)
    if data!=None:
        if data==[]:
            print(data)
            playing_as='x'
            connect.send_data([{'turn': t}])
            connect.send_data([{x: y}])
            playb.setx(5466)
            connected=True
        elif data[0]['b'] == None:
            set_player('b','x')
            playing_as='x'
            set_turn('x')
            playb.setx(3627)
            connected=True
        elif data[0]['a'] != None:
            set_player('b','o')
            playing_as='o'
            set_turn('o')
            playb.setx(5466)
            connected=True
        elif data[0]['b'] != None:
            set_player('a','o')
            set_turn('o')
            playing_as='o'
            playb.setx(5466)
            connected=True
        if data!=[]:
            if data[0]['b'] != None and data[0]['a'] != None:
                clear()
    else:
        print("Data: null")
    

playb = turtle.Turtle()
turtle.register_shape('play.gif')
playb.shape('play.gif')
playb.penup()
playb.goto(0, 0)
playb.onclick(inito)
screen.update()


# Ask for player names
player1_name = screen.textinput("Player 1 Name", "Enter Player 1's name:")
player2_name = screen.textinput("Player 2 Name", "Enter Player 2's name:")

moves=0



    

# Function to draw the board of Tic Tac Toe
def draw_board():
    # Draw the Tic Tac Toe board
    turtle.pencolor('green')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3, -1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3, 1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1, -3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

# Function to draw circle (representing O's turn)
def draw_circle(x, y):
    turtle.up()
    turtle.goto(x, y - 0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.75, steps=100)

# Function to draw X (representing X's turn)
def draw_x(x, y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x - 0.75, y - 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y + 0.75)
    turtle.up()
    turtle.goto(x - 0.75, y + 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y - 0.75)

def draw_piece(i, j, p):
    if p == 0:
        return
    x, y = 2 * (j - 1), -2 * (i - 1)
    if p == 1:
        draw_x(x, y)
    else:
        draw_circle(x, y)

# Function to decide when to call draw_x(x,y) and draw_circle(x,y)
def draw(b):
    print('called draw()')
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i, j, b[i][j])
    screen.update()
    
def update(data):
    for k in data:
        if k['move']!=playing_as and k['move'] != None:
            print(k['row'], k['column'])
            row=int(k['row'])
            col=int(k['column'])
            b[row][col] = atoi(playing_as, True)
    
    
    
def con():
    global data, turn
    threading.Timer(1.0, con).start()
    datai=connect.get_all_data()
    data=datai['Data']
    update(data)
    turn=get_turn()

con()

# Function to decide if the game has reached a terminal condition or not
def gameover(b):
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9: return 3
    else: return 0
    




# Function  to detect click on the screen
def play(x, y):
    global moves, playing_as, data
    global connected
    global turn
    global b
    if gameover(b) > 0:
        
        winner = ""
        if gameover(b) == 1:
            winner = player1_name
        elif gameover(b) == 2:
            winner = player2_name

        play_again = screen.textinput("Game Over!", f"{winner} won!\nPlay again? (yes/no)")
        if play_again and play_again.lower() == "yes":
            reinitialize_game()
        else:
            screen.bye()  # Close the game window
            return

    
    
    
    
    datai=[]
    
    if turn == playing_as and connected==True and draw!=[]:
        
        i = 3 - int(y + 5) // 2
        j = int(x + 5) // 2 - 1
        if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0:
            return
        
        datai=[{'move':turn,'row':i,'column':j}]
        
        b[i][j] = atoi(playing_as, False)
        print('turn', turn)
        print('pas', playing_as)
        draw(b)
        
        moves=+1
        if playing_as == 'x':
            turn='o'
            set_turn('o')
        elif playing_as == 'o':
            turn='x'
            set_turn('x')
        print('iturn', turn)
    
    if datai!=[]:
        connect.send_data(datai)
        
        
    
    r = gameover(b)
    if r == 1:
        screen.textinput("Game over!", "X won!", winner)
    elif r == 2:
        screen.textinput("Game over!", "O won!", winner)
    elif r == 3:
        screen.textinput("Game over!", "Tie!")

# Function to reinitialize the screen when player selects yes to play again
def reinitialize_game():
    
    global b
    global player1_name
    global player2_name
    global turn
    turtle.clear()
    
    b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    turn = 'x'
    draw(b)
    screen.update()
    player1_name = screen.textinput("Player 1 Name", "Enter Player 1's name:")
    player2_name = screen.textinput("Player 2 Name", "Enter Player 2's name:")
    
screen.onclick(play)
turn=get_turn()
print(turn, 'ogoewogo')
turtle.mainloop()

############################################################################