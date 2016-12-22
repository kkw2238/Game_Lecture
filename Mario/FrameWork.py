from pico2d import *
import time


class GameState:
    def __init__(self, state):
        self.ENTER = state.ENTER
        self.EXIT = state.EXIT
        self.PAUSE = state.PAUSE
        self.Handle_Event = state.Handle_Event
        self.UPDATE = state.UPDATE
        self.DRAW = state.DRAW



class TestGameState:

    def __init__(self, name):
        self.name = name

    def ENTER(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def handle_events(self, frame_time):
        print("State [%s] handle_events(%f)" % (self.name, frame_time))

    def update(self, frame_time):
        print("State [%s] update(%f)" % (self.name, frame_time))

    def draw(self, frame_time):
        print("State [%s] draw(%f)" % (self.name, frame_time))



running = None
stack = None


def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.ENTER()



def push_state(state):
    global stack
    stack.append(state)
    state.ENTER()



def pop_state():
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()

    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False
    close_canvas()


def run(start_state):
    global running, stack
    running = True
    open_canvas(962, 700 ,sync = True)
    stack = [start_state]
    start_state.ENTER()
    current_time = time.clock()
    while (running):
        frame_time = time.clock() - current_time
        current_time += frame_time
        stack[-1].handle_events(frame_time)
        stack[-1].UPDATE(frame_time)
        stack[-1].DRAW(frame_time)

    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def reset_time():
    global current_time
    current_time = time.clock()

def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)



if __name__ == '__main__':
    test_game_framework()