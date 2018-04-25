from libdw import sm

from q5_avatar import Avatar
from q6_world import Map

import copy

class DW2Game(sm.SM):
	def __init__(self, avatar, world):
		self.startState = (copy.deepcopy(avatar), copy.deepcopy(world))

	def getNextValues(self, state, inp):
		mode, direction = inp
		avatar, world = state
		new_avatar, new_world = copy.deepcopy(avatar), copy.deepcopy(world)

		current_pos = new_avatar.getPosition()
		new_position = None # Initialize next position as None

		if direction == 'up':
			new_position = (current_pos[0], current_pos[1] - 1)
		elif direction == 'down':
			new_position = (current_pos[0], current_pos[1] + 1)
		elif direction == 'left':
			new_position = (current_pos[0] - 1, current_pos[1])
		elif direction == 'right':
			new_position = (current_pos[0] + 1, current_pos[1])

		next_pos = new_world.whatIsAt(new_position)

		if mode == 'move':
			if next_pos == 'Empty':
				new_avatar.setPosition(new_position)
			elif next_pos == 'Food':
				new_avatar.setPosition(new_position)
				heal_amt = new_world.getFoodEnergy(new_position)
				new_avatar.heal(heal_amt)
				new_world.eatFood(new_position)
			elif next_pos == 'Wall':
				pass
			elif next_pos == 'Enemy':
				attack_amt = new_world.getEnemyAttack(new_position)
				new_avatar.attacked(attack_amt)
			elif next_pos == 'Exit':
				new_avatar.setPosition(new_position)
		elif mode == 'attack':
			if next_pos == 'Enemy':
				# Remove enemy
				new_world.removeEnemy(new_position)

		return ((new_avatar, new_world), (new_avatar.getName(), new_avatar.getPosition(), new_avatar.getHP()))

	def done(self, state):
		avatar, world = state
		return world.whatIsAt(avatar.getPosition()) == 'Exit'

world2={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2): -2, (5,2): 0, (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0,}

# print 'test 1'
# inp=[('move','down'),('attack','down'),('move','down'),( 'move','down'), ('move','down'),('move','right'),('move','right'),('move','right'),('move','down'), ('move','down')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp) == [('John', (1, 1), 98), ('John', (1, 1), 98), ('John', (1, 2), 98), ('John', (1, 3), 98), ('John', (1, 4), 98), ('John', (2, 4), 98), ('John', (3, 4), 98), ('John', (4, 4), 98), ('John', (4, 5), 98)]

# print 'test 2'
# inp=[('move','left'),('move','right'),('move','right'),('move','right'), ('move','right'),('move','down'),('move','down'),('move' ,'down'),('move','up')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp) == [('John', (1, 1), 100), ('John', (2, 1), 100), ('John', (3, 1), 100), ('John', (4, 1), 100), ('John', (4, 1), 100), ('John', (4, 2), 100), ('John', (4, 3), 100), ('John', (4, 4), 100), ('John', (4, 3), 100)]

# print 'test 3'
# inp=[('move','right'),('move','right'),('move','right'), ('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp) == [('John', (2, 1), 100), ('John', (3, 1), 100), ('John', (4, 1), 100), ('John', (4, 2), 100), ('John', (3, 2), 100), ('John', (2, 2), 100), ('John', (2, 2), 98), ('John', (2, 2), 98), ('John', (1, 2), 98)]

# print 'test 4'
# inp=[('move','right'),('move','right'),('move','right'), ('move','down'),('move','left'),('move','left'),('move','left'), ('attack','left'),('move','left'),('move','left'),('move','down'),('move','right')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp) == [('John', (2, 1), 100), ('John', (3, 1), 100), ('John', (4, 1), 100), ('John', (4, 2), 100), ('John', (3, 2), 100), ('John', (2, 2), 100), ('John', (2, 2), 98), ('John', (2, 2), 98), ('John', (1, 2), 98), ('John', (1, 2), 98), ('John', (1, 3), 98), ('John', (2, 3), 101)]

# print 'test 5'
# inp=[('move','right'),('move','right'),('move','right'), ('move','down'),('move','left'),('move','left'),('move','left'), ('attack','left'),('move','left'),('move','left'),('move','down'), ('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),('move','down')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp) == [('John', (2, 1), 100), ('John', (3, 1), 100), ('John', (4, 1), 100), ('John', (4, 2), 100), ('John', (3, 2), 100), ('John', (2, 2), 100), ('John', (2, 2), 98), ('John', (2, 2), 98), ('John', (1, 2), 98), ('John', (1, 2), 98), ('John', (1, 3), 98), ('John', (2, 3), 101), ('John', (3, 3), 101), ('John', (4, 3), 101), ('John', (4, 4), 101), ('John', (4, 5), 101)]

# print 'test 6'
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# g.start()
# n,o=g.getNextValues(g.startState,('move','right'))
# ans = g.state[0].getPosition() == n[0].getPosition()
# print ans, g.state[0].getPosition(), n[0].getPosition()


