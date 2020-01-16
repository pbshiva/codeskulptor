#Stop watch reflex game

# Import modules
import simplegui

# Global state
time = 0
hits =  0
bulls_eye = 0
timer_state = False

# HELPERS
# Time to Minute:Seconds.MilliSecond formatter
def format(v):
    m = v // 600
    r = v - m * 600
    sec = str(r)
    if len(sec) == 1:
        sec = '00'+sec
    elif len(sec) == 2:
        sec = '0' + sec
    return str(m)+':'+sec[0:2]+'.'+sec[-1]

# Reflex check
def check_reflex():
    global hits
    global bulls_eye
    hits += 1
    if(time % 10 == 0):
        bulls_eye += 1

# Handler for timer
def tick():
    global time
    time+=1

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(format(time), [100,80], 36, "Red")
    if hits == 0:
        canvas.draw_text("Try stopping at __.0 seconds",[20,20],20,"white")
    else:
        canvas.draw_text("Reflex Factor:"+str(bulls_eye)+"/"+str(hits),[150,20],20,"white")
    
# Handlers for timer control
def startTimer():
    global timer_state
    timer_state = True
    timer.start()
    
def stopTimer():
    global timer_state
    if timer_state:
        check_reflex()
        timer.stop()
        timer_state = False

def resetTimer():
    timer.stop()
    global time
    time = 0
    global hits
    hits = 0
    global bulls_eye
    bulls_eye = 0
    global timer_state
    timer_state = False

# Create a frame 
frame = simplegui.create_frame("StopWatch Game", 300, 120)

# Register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
start = frame.add_button('Start',startTimer, 100)
stop = frame.add_button('Stop',stopTimer,100)
reset = frame.add_button('Reset',resetTimer,100)


# Start the frame
frame.start()
