import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    startState=('forward',0.0)
    def getNextValues(self, state, inp):
        state, orig_angle = state
        angle = util.fixAnglePlusMinusPi(inp.odometry.theta)
        front_dist = inp.sonars[2]
        eps = 0.01
        if state=='forward':
            if front_dist <=0.5:
                next_state = ('rotate', angle)
                forward = 0.0
                rotation = 0.1
            else:
                next_state = ('forward', angle)
                forward = 0.1
                rotation = 0.0
        elif state == 'rotate':
            if not util.nearAngle(abs(angle-orig_angle), math.pi/2.0,eps):
                next_state = ('rotate', orig_angle)
                forward = 0.0
                rotation = 0.1
            else:
                next_state = ('forward', angle)
                forward = 0.1
                rotation = 0.0
        print next_state, forward, rotation
        return (next_state, io.Action(fvel = forward, rvel = rotation))

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=False) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass