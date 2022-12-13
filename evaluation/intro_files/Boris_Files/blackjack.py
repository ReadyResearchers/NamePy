# Mini-project #6 - Blackjack
# Author: Boris Litinsky
# Date: 10/25/2014

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        self.front_image = True
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return VALUES[self.rank]
        
    def draw(self, canvas, pos):
        if self.front_image == True:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            card_loc = (CARD_CENTER[0],CARD_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)    
        
# define hand class
class Hand:
    def __init__(self):
        self.card_hand = []
        self.hand_value = 0

    def __str__(self):
        self.string = ""
        for card in self.card_hand:
            self.string += str(card) + " "
        return self.string

    def add_card(self, card):
        self.card_hand.append(card)

    def get_value(self):
        self.hand_value = 0
        for card in self.card_hand:
            self.hand_value += card.get_value()
        for card in self.card_hand: # add 10's for each ace in the hand
            if (card.get_rank() == 'A') and ((self.hand_value + 10) <= 21):
                self.hand_value += 10
        return self.hand_value

    def show_front_card(self):
        self.card_hand[0].front_image = True
        
    def show_back_card(self):
        self.card_hand[0].front_image = False
        
    def draw(self, canvas, pos):
        for card in self.card_hand:
            x_pos = pos[0] + CARD_SIZE[0] * self.card_hand.index(card)
            y_pos = pos[1]            
            card.draw(canvas, [x_pos,y_pos]) 
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit,rank)
                self.card_deck.append(card)                

    def shuffle(self):
        random.shuffle(self.card_deck)

    def deal_card(self):
        card = self.card_deck.pop()
        return(card)
    
    def __str__(self):
        self.string = ""
        for card in self.card_deck:
            self.string += str(card) + " "
        return self.string

#define event handlers for buttons
def deal():
    global in_play, deck, plrHand, dlrHand, dlrMsg, score, plrMsg
      
    # create and shuffle new card deck and create player and dealer hands
    deck = Deck()		# create a new 52-card deck
    deck.shuffle()		# shuffle card deck
    plrHand = Hand()
    dlrHand = Hand()
    dlrMsg = ""
    plrMsg = ""

    # if a game is already in progress and a deal() is clicked, penalize player
    if in_play == True:
        score -= 1
    in_play = True   # game started
        
    # deal two cards to player and dealer
    for i in range(2):
        plrHand.add_card(deck.deal_card())
        dlrHand.add_card(deck.deal_card())    

    dlrHand.show_back_card()
    plrMsg = "Hit or Stand?"
          
def hit():
    global in_play, deck, plrHand, dlrMsg, score, in_play, plrMsg
    plrMsg = ""
    
    # if the hand is in play, hit the player
    if in_play == True:
        plrHand.add_card(deck.deal_card())
        if plrHand.get_value() > 21:
            dlrHand.show_front_card()
            dlrMsg = "Dealer wins! Player Busted!"
            score -= 1
            in_play = False
            plrMsg = "New Deal?"
                        
def stand():
    global in_play, deck, dlrHand, plrHand, dlrMsg, score, plrMsg  
    plrMsg = ""
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while True:
            if dlrHand.get_value() <= 16:
                # dealer hits
                dlrHand.add_card(deck.deal_card())
            else:
                break

        # if busted, assign a message to outcome, update in_play and score 
        dlrHand.show_front_card()
        if dlrHand.get_value() == 21:
            dlrMsg = "Dealer wins! Blackjack!"
            score -= 1         
        elif dlrHand.get_value() > 21:
            dlrMsg = "Player wins! Dealer Busted!"
            score += 1   
        elif dlrHand.get_value() >= plrHand.get_value():
            dlrMsg = "Dealer wins!"
            score -= 1
        else:
            if plrHand.get_value() == 21:
                dlrMsg = "Player wins! Blackjack!"
            else:
                dlrMsg = "Player wins!"
            score += 1
        in_play = False
        plrMsg = "New Deal?"

# draw handler    
def draw(canvas):
    global plrHand, dlrHand, dlrMsg, score, plrMsg
    
    # draw dealer's and player's card hands
    dlrHand.draw(canvas, [100, 100])
    plrHand.draw(canvas, [100, 300])
    
    # draw text messages
    canvas.draw_text("Dealer", (100,  80), 24, 'Black')
    canvas.draw_text(dlrMsg,   (200,  80), 24, 'Black')    
    canvas.draw_text("Player", (100, 280), 24, 'Black')
    canvas.draw_text(plrMsg,   (200, 280), 24, 'Black')
    canvas.draw_text("Blackjack", (200, 40), 36, 'Black')
    canvas.draw_text("Score:" + str(score), (500, 40), 24, 'Red')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()