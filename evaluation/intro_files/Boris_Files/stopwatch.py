# Stopwatch The Game

# Import modules
import simplegui

# Global state
message = "0:00:0"
message_pos = [200, 200]

score = "0/0"
score_pos = [400, 40]
wins = 0
attempts = 0

width = 500
height = 500
interval = 100
counter = 0
running = False

#reset the stopwatch
def reset_watch():
    global counter
    global running
    global wins
    global attempts
    global message
    global score
    
    counter = 0
    wins = 0
    attempts = 0
    message = "0:00:0"
    score = "0/0"
    timer.stop()
    running = False
    
#start the stopwatch
def start_watch():
    global running
    timer.start()
    running = True

#stop the stopwatch
def stop_watch():
    global running
    global wins
    global attempts
    global score
    timer.stop()
    if (running == True and (counter % 10) == 0):
        attempts += 1
        wins += 1
    elif (running == True):
        attempts += 1
    score = str(wins) + "/" + str(attempts)    
    running = False

# return string with format A:BC:D
def format(t):
    d = t % 10
    c = (t / 10) % 10
    b = (t / 100) % 6
    a = (t / 600) % 10
    time = str(a) + ":" + str(b) + str(c) + ":" + str(d)
    return time
    
# Handler for timer
def tick():
    global counter
    global message
    counter += 1
    message = format(counter)
       
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, message_pos, 36, "White")
    canvas.draw_text(score  , score_pos,   36, "Red")

# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

frame.add_button("Start",start_watch)
frame.add_button("Stop", stop_watch)
frame.add_button("Reset",reset_watch)

# Start the frame animation
frame.start()