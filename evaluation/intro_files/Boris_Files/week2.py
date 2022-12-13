import simplegui

# Globals
counter = 0

# Helper Functions
def increment():
    global counter
    count += 1

# Classes

# Define Event Handlers
def tick():
    increment()
    print (counter)

# Create a Frame
frame = simplegui.create_timer("Simple Gui Test", 100, 100)

# Register Event Handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Clock me!",tick)

# Start Frame & Timers
frame.start()
timer.start()