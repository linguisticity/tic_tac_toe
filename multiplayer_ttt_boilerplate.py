import turtle
################################################################
#TODO:		Import the sheet_dot_best_manager file below	   #
################################################################


################################################################

###################################################################################
#TODO: initialize global variables	to None (current_turn, player, connect, etc) #
###################################################################################


###################################################################################


def initialize_screen():
	global b,turn, screen

	screen = turtle.Screen() #Return the singleton screen object. If none exists at the moment, create a new one and return it, else return the existing one.
	screen.setup(800,800) #Set the size and position of the main window.
	screen.title("Tic Tac Toe - e-Yantra") #Set title of turtle-window
	screen.setworldcoordinates(-5,-5,5,5) #Set up a user defined coordinate-system
	screen.bgcolor('black') #Set or return backgroundcolor of the TurtleScreen.
	screen.tracer(n=2,delay=10) #Turns turtle animation on/off and set delay for update drawings.
	turtle.speed(0)
	turtle.showturtle()
	turtle.resetscreen()
	b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]  # Nested list representing the value inside each box of the game.
	draw_board() # Draw the board for the first time.


def draw_board():
	turtle.pencolor('green') #Set pen color
	turtle.pensize(10) #Set pen size
	turtle.up()	#It means turtle will not draw if it moves
	turtle.goto(-3,-1) #Move the portal to (x,y) position
	turtle.seth(0) #Set heading of Turtle to 0
	turtle.down() #After this command, turtle will draw when it moves
	turtle.fd(6) #Move turtle forward by 6 units
	turtle.up() 
	turtle.goto(-3,1)
	turtle.seth(0)
	turtle.down()
	turtle.fd(6)
	turtle.up()
	turtle.goto(-1,-3)
	turtle.seth(90)
	turtle.down()
	turtle.fd(6)
	turtle.up()
	turtle.goto(1,-3)
	turtle.seth(90)
	turtle.down()
	turtle.fd(6)
	turtle.update()


def draw_circle(x,y): #Following commands will help to draw o about the given center i.e. (x,y)
	turtle.up()
	turtle.goto(x,y-0.75)
	turtle.seth(0)
	turtle.color('red')
	turtle.down()
	turtle.circle(0.75)


def draw_x(x,y): #Following commands will help to draw x about the given center i.e. (x,y)
	turtle.color('blue')
	turtle.up()
	turtle.goto(x-0.75,y-0.75)
	turtle.down()
	turtle.goto(x+0.75,y+0.75)
	turtle.up()
	turtle.goto(x-0.75,y+0.75)
	turtle.down()
	turtle.goto(x+0.75,y-0.75)


def draw_piece(i,j,p):
	if p==0: return #'p' or b[i][j] corresponds to empty cell. Since cell is empty i.e. contains 0, there is no need to draw
	x,y = 2*(j-1), -2*(i-1) 
	if p==1:  #As per the earlier convention, if 'p' is 1, we need to draw x otherwise o
		draw_x(x,y)
	else:
		draw_circle(x,y)


def draw(i,j,b):
	draw_piece(i,j,b)
	screen.update() # Perform an update on the screen


# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b):
	# Conditions required to check the winner.
	if b[0][0]>0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
	if b[1][0]>0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
	if b[2][0]>0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
	if b[0][0]>0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
	if b[0][1]>0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
	if b[0][2]>0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
	if b[0][0]>0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
	if b[2][0]>0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
	p = 0
	for i in range(3):
		for j in range(3):
			p += (1 if b[i][j] > 0 else 0) # 'p=p+1 if b[i][j]>0 else p=p+0'
	if p==9: return 3
	else: return 0
	

def play(x,y):
	# print("X:Y",x,y)
	# Cordinate system before conversion (Top left is (-5,5) and bottom right is (5,-5)):
	'''
	y
	↑
	|
	|
	.-----→x
	(-5,5)						   (5,5)
	.----------------------------------.
	|				 |				   |
	|				 |				   |
	|				 |				   |	
	|				 |(0,0)			   |
	|----------------.-----------------|
	|				 |				   |
	|				 |				   |
	|				 |				   |
	|				 |				   |
	.----------------------------------.
	(-5,-5)						  (5,-5)
	'''
	# Cordinate system after conversion (Top left is (0,0) and bottom right is (2,2)):
	'''
	.----→j		|	  |
	|		0,0 |	  | 2,0
	|	   _____|_____|_____
	↓			|	  |
	i			| 1,1 |
		   _____|_____|_____
				|	  | 
			0,2	|	  | 2,2
				|	  |
	'''
	# Conversion from one coordinate system to another:
	'''
	Conversion of x to j:
	 x	|	j
	---------
	-3	|	0
	-1	|	1
	 1	|	2
	Assume x=aj+b,
	Solve simultaneously for the above limits
	and obtain the value of a and b
	Conversion of y to i:
	 y	|	i
	---------
	 3	|	0
	 1	|	1
	-1	|	2
	Assume y=ai+b,
	Solve simultaneously for the above limits
	and obtain the value of a and b.
	'''
	global turn, player_1, player_2,continue_playing,b, current_turn
	i=-(int(y-3))//2
	j=(int(x+3))//2

	if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0: 
		return # Condition will be true if user will click outside the designated area 
	if turn == 'x': 
		b[i][j] = 1	#Assign b[i][j] as 1 and turn as 'o'
	else: 
		b[i][j] = 2	#Assign b[i][j] as 2 and turn as 'x'
	
	current_turn = turn
	################################################################
	#TODO:		Send data to store in the sheet					   #
	################################################################


	################################################################
	draw_and_check(i, j)

def draw_and_check(i, j):
	global b, continue_playing

	draw(i,j,b[i][j])
	r = gameover(b)
	if r==1:
		continue_playing=screen.textinput("X won!","Type 'yes'/'no' to play again.")
		reinitialize_screen()
	elif r==2:
		continue_playing=screen.textinput("O won!","Type 'yes'/'no' to play again.")		
		reinitialize_screen()
	elif r==3:
		continue_playing=screen.textinput("Tie!","Type 'yes'/'no' to play again.")
		reinitialize_screen()

def reinitialize_screen():
	global b,turn,continue_playing

	if(continue_playing is not None and continue_playing.lower()=='yes'):
		turtle.resetscreen()
		b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]  # Nested list representing the value inside each box of the game.
		draw_board() # Draw the board for the first time.
		clear_sheet()
	else:
		turtle.bye()


def input_player():
	global player, screen, turn
	player = input("Play as X or O : ")
	if player == 'X' or player == 'x':
		turn = 'x'
	elif player == 'O' or player == 'o':
		turn = 'o'

def refresh_sheet():
	global connect, b, last_move,current_turn
	print("Refreshing....")
	################################################################
	#TODO: Get data from the sheet and redraw if there is new data #
	################################################################


	################################################################
	

def clear_sheet():
	global connect
	print("Deleting previous data...")
	################################################################
	#TODO: Delete all previous data from the sheet				   #
	################################################################


	################################################################
	

if __name__ == "__main__":
	initialize_screen()
	screen.onclick(play) #Bind function to mouse-click event on canvas. Coordinates of the click are passed as an argument to the function.
	turtle.mainloop()