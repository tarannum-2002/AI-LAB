import numpy as np
import time
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

class Node():
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent= parent
        self.action = action
        self.depth = depth

        self.move_up = None
        self.move_down = None
        self.move_left= None
        self.move_right= None
    
        
    def move_down(self, index):
        pass
        







    def DLS(self, depth):
        leaves = LifoQueue()
        leaves.put(self.start)
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            if actual.goalState():
                return actual
            elif actual.depth is not depth:
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())

    def IDS(self):
        depth = 0
        result = None
        while result == None:
            result = self.depthLimited(depth)
            depth +=1
        return result
        

test = np.array([1,3,4,8,6,4,7,5,0])
goal_state = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)

initial_state = test
print(initial_state)
print(goal_state)



root_node = Node(state = initial_state, parent=None, action=None, depth=0)

  












