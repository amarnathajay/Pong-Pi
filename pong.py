from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
y = 4

score = 0

ball_position = [3,3]
ball_velocity = [1,1]

def draw_bat():
    sense.set_pixel(0, y, 255, 255, 255)
    sense.set_pixel(0, y + 1, 255, 255, 255)
    sense.set_pixel(0, y - 1, 255, 255, 255)

def move_up(event):
    global y
    if event.action == 'pressed' and y > 1:
        y -= 1

def move_down(event):
    global y
    if event.action == 'pressed' and y < 6:
        y += 1

def draw_ball():
    global score
    sense.set_pixel(ball_position[0], ball_position[1],0,0,255)
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 7:
       ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] == 0 or ball_position[1] == 7:
       ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 0:
        finscore = str(score)
        sense.show_message("You Lose! Score = " + finscore, text_colour=(255,0,0))
        quit()
    if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y + 1:
        ball_velocity[0] = -ball_velocity[0]
        score = score + 1
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
    sense.clear(0, 0, 0)
    draw_bat()
    draw_ball()
    sleep(0.25)
    
