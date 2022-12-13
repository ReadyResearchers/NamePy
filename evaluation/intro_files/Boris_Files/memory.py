##################################################################
# Memory Game
# Intro to Python Class/Coursera
# Date: 10/19/2014
# Author: Boris Litinsky
##################################################################

import simplegui
import random

# define global variables
WIDTH  = 60
HEIGHT = 100
cards = []
exposed = []
matched = []
history = []
turn = 0
state = 0

# initialize new game
def new_game():
    global state, cards, exposed, matched, turn, history
    cards = range(8) * 2
    random.shuffle(cards)
    exposed = [False] * 16
    matched = [False] * 16
    state = 0
    history = []
    turn = 0

# process mouse clicks    
def click(pos):
    global exposed, matched, turn, history, state
    
    # using mouse position, determine the index into the card deck
    index = int(pos[0] // WIDTH)
    
    # check that the index is within legal range
    if index >= 0 and index < len(exposed):
        
        # expose card clicked on
        exposed[index] = True
        
        # ignore clicks on the same card
        if matched[index] == False or exposed[index] == False:
            #print "index",index,"history",history
            history.append(index)    
            
            if len(history) >= 2:
                if cards[history[-1]] == cards[history[-2]]:
                    matched[history[-1]] = True
                    matched[history[-2]] = True
            if state == 0:
                state = 1
            elif state == 1:
                state = 2
                turn += 1
            else:
                # flip two older cards back
                exposed[history[-3]] = False
                exposed[history[-2]] = False
                state = 1

    label.set_text("Turn: " + str(turn))        
    #print "num",num,"history",history,"state",state,"matched",matched
               
def draw(canvas):
    global cards, exposed, matched
    for i in range(16):
        card = cards[i]
        if matched[i] == True:
            canvas.draw_text(str(card),[10+WIDTH*i, HEIGHT//2], 60, "Red")
        elif exposed[i] == True:
            canvas.draw_text(str(card),[10+WIDTH*i, HEIGHT//2], 60, "White")
        else:
            canvas.draw_polygon([[0+WIDTH*i,0],[0+WIDTH*i,HEIGHT],[WIDTH+WIDTH*i,HEIGHT],[WIDTH+WIDTH*i,0]],10,"Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory states", 16 * WIDTH, 100)
frame.add_button("Restart", new_game, 200)
frame.set_mouseclick_handler(click)
label = frame.add_label("Turn: " + str(turn))

# register event handlers
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()