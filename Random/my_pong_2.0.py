# Implementation of classic arcade game Pong

#import module
import pygame
import random
from tkinter import*

#pygame specific locals/constants
from pygame.locals import*

#root = Tk() #defines a new window
#root.geometry("200x200") #sets size of the window
#root.title('Restart Game') #title of window
#frame1 = Frame(root).grid(row = 0, column = 0) 
    
#initialize
pygame.init()

#create canvas
canvas = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PongPong")

#set fonts and color/craete new Font object 
fontObj = pygame.font.Font(pygame.font.match_font('timesnewroman'), 32)

gold_color = pygame.Color(255, 215, 0)
white_color = pygame.Color(255, 255, 255)
                     

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PADDLE_ACCEL = 12

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [random.randrange(2,6), -random.randrange(1,4)]
    if not right:
        ball_vel[0] = -ball_vel[0]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos= HEIGHT/2 - HALF_PAD_HEIGHT
    paddle2_pos= HEIGHT/2 - HALF_PAD_HEIGHT
    paddle1_vel = 0.0
    paddle2_vel = 0.0
    ball_init(True)
    

def draw_handler(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel
    color = random.choice([pygame.Color(255, 215, 0), pygame.Color(255, 255, 255), pygame.Color(28, 219, 38), pygame.Color(19, 243, 213)])
    paddle1_color = pygame.Color(243, 19, 64)
    paddle2_color = pygame.Color(19, 161, 243)
    #clear canvas
    canvas.fill((0, 0, 0))
 
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos +paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos+paddle1_vel < HEIGHT - HALF_PAD_HEIGHT :
        paddle1_pos = paddle1_pos + paddle1_vel    
        
    if paddle2_pos+paddle2_vel >= 0.1*HALF_PAD_HEIGHT and paddle2_pos+paddle2_vel < HEIGHT - 2*HALF_PAD_HEIGHT:
        paddle2_pos = paddle2_pos + paddle2_vel            
        
    # draw mid line and gutters
    pygame.draw.line(canvas, white_color, [WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(canvas, white_color, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, white_color, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    
    # draw paddles
    pygame.draw.line(canvas, paddle1_color, [HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH)
    pygame.draw.line(canvas, paddle2_color, [(WIDTH - 1) - HALF_PAD_WIDTH, paddle2_pos],
                     [(WIDTH - 1) - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH)
        
    # update ball
    ball_pos[0] = ball_pos[0]+ball_vel[0]
    ball_pos[1] = ball_pos[1]+ball_vel[1]
    if ball_pos[1]-BALL_RADIUS <= 0 or ball_pos[1]+BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    #left gutter    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if  ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0] / 10
            ball_vel[1] += ball_vel[0] / 10
        else:
            score2 += 1
            ball_init(True)
    #right gutter        
    if ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0] / 10
            ball_vel[1] += ball_vel[0] / 10      
        else:
            score1 += 1
            ball_init(False)
 
            
    # draw ball and scores
    canvas.blit(fontObj.render(str(score1), True, gold_color), (125, 25))
    canvas.blit(fontObj.render(str(score2), True, gold_color), (450, 25))
    pygame.draw.circle(canvas, gold_color, [int(ball_pos[0]), int(ball_pos[1])], BALL_RADIUS)
    
    #update the display
    pygame.display.update()
    
        
def keydownnn(key):
    global paddle1_vel, paddle2_vel
   
    if pygame.K_w == key:
    	paddle1_vel -= PADDLE_ACCEL
    elif pygame.K_s == key:
    	paddle1_vel += PADDLE_ACCEL
    elif pygame.K_UP == key:
    	paddle2_vel -= PADDLE_ACCEL
    elif pygame.K_DOWN == key:
    	paddle2_vel += PADDLE_ACCEL
    #restart
    elif pygame.K_r == key:
    	init()
        
def keyup(key):
    global paddle1_vel, paddle2_vel
   
    if pygame.K_w == key:
    	paddle1_vel += PADDLE_ACCEL
    elif pygame.K_s == key:
    	paddle1_vel -= PADDLE_ACCEL
    elif pygame.K_UP == key:
    	paddle2_vel +=PADDLE_ACCEL
    elif pygame.K_DOWN == key:
    	paddle2_vel -=PADDLE_ACCEL

# register event handlers for control elements
 
#b_r = Button(frame1, text= 'Restart Game', command=init, width = 20, pady =2).grid(row =0, column =0)      
init()



# ------------------------CodeSkulptor Port Ends-------------------------

# call this function to start everything
# could be thought of as the implemntation of the CodeSkulptor frame .start() method.
def main():
    # initialize loop until quit variable
    running = True
    
    # create our FPS timer clock
    clock = pygame.time.Clock()    

#---------------------------Frame is now Running-----------------------------------------
    
    # doing the infinte loop until quit -- the game is running
    while running:
        
        # event queue iteration
        for event in pygame.event.get():
            
            # window GUI ('x' the window)
            if event.type == pygame.QUIT:
                running = False

            # input - key and mouse event handlers
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # just respond to left mouse clicks
                #if pygame.mouse.get_pressed()[0]:
                 #   mc_handler(pygame.mouse.get_pos())
                
            elif event.type == pygame.KEYUP:
                keyup(event.key)

            elif event.type == pygame.KEYDOWN:
                keydown(event.key)
            
                
       # # the call to the draw handler
        draw_handler(canvas)
        
        # FPS limit to 60 -- essentially, setting the draw handler timing
        # it micro pauses so while loop only runs 60 times a second max.
        clock.tick(60)
        
#-----------------------------Frame Stops------------------------------------------

    # quit game -- we're now allowed to hit the quit call
    pygame.quit ()

# this calls the 'main' function when this script is executed
if __name__ == '__main__': main() 



