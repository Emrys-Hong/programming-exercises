from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world

class MySMClass(sm.SM):
    start_state=None
    def get_next_values(self, state, inp):
        # These two lines is to stop the robot
        # by pressing the backward button.
        # This only works when using the real robot.
        # It will not work in simulator.
        if inp.button_backward:
            return 'halt', io.Action(0,0)
        

        
        #ground = inp.prox_ground.reflected
        #ground1 = inp.prox_ground.ambiant
        ground2 = inp.prox_ground.delta
        #left = ground[0]
        #right = ground[1]
        #right1 = ground1[1]
        left2 = ground2[0]
        right2 = ground2[1]
        if left2 > 500:
            state = 'white'
            forward = 0.2
        else:
            state = 'black'
            forward = 0.0
        
        #io.Action(fv=0.0, rv=0.0) if state == 'black' else io.Action(fv=0.2, rv=0.0)
        return state, io.Action(fv=forward, rv=0.0)

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self,state):
        if state=='halt':
            return True
        else:
            return False

MySM=MySMClass()

############################

m=ThymioSMReal(MySM, thymio_world)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
