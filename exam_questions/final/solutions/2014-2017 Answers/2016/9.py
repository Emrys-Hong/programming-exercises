from q5_avatar import Avatar
from q8_world import Map

from libdw import ucSearch

import copy

def calculate_next_path(pos, cost, world):
	if world.whatIsAt(pos) == 'Exit':
		return 

def getGoal(world):
	for key in world:
		if world[key] == 'x':
			return key

def findPath(avatar, world):
	searchMap = world.getSearchMap()
	initialState = avatar.getPosition()
	goal = getGoal(world.world)
	cost = 0

	def goalTest(position):
		return goal == position

	def successor(state, action):
		if action in searchMap[state]:
			return searchMap[state][action]
		else:
			return (None, None)

	path = ucSearch.search(initialState, goalTest, [0, 1, 2, 3], successor)

	if path[1]:
		return path
	else:
		return None


world={(0,0):0, (1,0):0, (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (5,1): 0,
(0,2):0, (1,2): -2, (5,2): 0, (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}

print 'test 1'
av=Avatar('John',position=(1,3))
m=Map(world)
print findPath(av,m)
