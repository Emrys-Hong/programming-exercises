import copy

class Map(object):
	def __init__(self, world):
		self.world = copy.deepcopy(world)

	def whatIsAt(self, position):
		''' checks what the map indicates at that particular position '''
		'''
		o if it is a character 'x', the function should return a string 'Exit',
		o if it is an integer 0, the function should return a string 'Wall',
		o if it is a positive integer, the function should return a string 'Food',
		o if it is a negative integer, the function should return a string 'Enemy',
		o if it is not found in the world dictionary, the function should return a string 'Empty'.
		'''
		if position in self.world:
			location_value = self.world[position]

			if location_value == 'x':
				# Exit
				return 'Exit'
			elif isinstance(location_value, int):
				# Integer
				if location_value == 0:
					return 'Wall'
				elif location_value > 0:
					return 'Food'
				elif location_value < 0:
					return 'Enemy'

		return 'Empty'

	def getEnemyAttack(self, position):
		''' returns the damaged value affecting the hp if there is an 'Enemy' in that particular position.
		If there is no enemy in that position, it should return a Boolean False
		'''
		if position in self.world:
			location_value = self.whatIsAt(position)
			if location_value == 'Enemy':
				return self.world[position]
		return False

	def getFoodEnergy(self, position):
		''' returns the energy value affecting the hp if there is a 'Food' in that particular position.
		If there is no food in that position, it should return a Boolean False.
		'''
		if position in self.world:
			location_value = self.whatIsAt(position)
			if location_value == 'Food':
				return self.world[position]

		return False

	def removeEnemy(self, position):
		''' checks if an 'Enemy' is in that position. If it is, it removes the 'Enemy' from the map
		by deleting the key-value pair in the dictionary world, and return a Boolean True.
		Otherwise, it will return a Boolean False. '''
		if position in self.world:
			location_value = self.whatIsAt(position)
			if location_value == 'Enemy':
				self.world.pop(position)
				return True
		return False

	def eatFood(self, position):
		''' checks if an 'Food' is in that position. If it is, it removes the 'Food' from the map
		by deleting the key-value pair in the dictionary world, and return a Boolean True.
		Otherwise, it will return a Boolean False. '''
		if position in self.world:
			location_value = self.whatIsAt(position)
			if location_value == 'Food':
				self.world.pop(position)
				return True
		return False

	def getExitPosition(self):
		''' If there is an 'Exit' in the map, the function returns the position as a tuple of two integers (x,y).
		Otherwise, it will return a None object. There is only one exit point in a map. '''

		# Check if x exists in the values of the world dict
		for position in self.world:
			if self.world[position] == 'x':
				return position

		return None

	def getSearchMap(self):
		# Find size of map
		offset = 0
		coordinates = []

		max_y, min_y, max_x, min_x = None, None, None, None
		for coordinate in self.world:
			if coordinate[0] < min_x or min_x == None:
				min_x = coordinate[0]
			if coordinate[0] > max_x or max_x == None:
				max_x = coordinate[0]

			if coordinate[1] < min_y or min_y == None:
				min_y = coordinate[1]
			if coordinate[1] > max_y or max_y == None:
				max_y = coordinate[1]

			# Determine max value
			if isinstance(self.world[coordinate], int) and self.world[coordinate] > offset:
				offset = self.world[coordinate]

		for i in range(min_x, max_x + 1):
			for j in range(min_y, max_y + 1):
				coordinates.append((i, j))

		positions_dict = {}

		for key in coordinates:
			value = {}
			directions = ['top', 'right', 'bottom', 'left']
			# Determine value for each position
			for i in range(4):
				current_pos = key
				direction = directions[i]
				if direction == 'top':
					new_position = (current_pos[0], current_pos[1] - 1)

					if current_pos[1] == min_y:
						continue
				elif direction == 'bottom':
					new_position = (current_pos[0], current_pos[1] + 1)

					if current_pos[1] == max_y:
						continue
				elif direction == 'left':
					new_position = (current_pos[0] - 1, current_pos[1])

					if current_pos[0] == min_x:
						continue
				elif direction == 'right':
					new_position = (current_pos[0] + 1, current_pos[1])

					if current_pos[0] == max_x:
						continue

				cost = abs(offset)
				nextValue = self.whatIsAt(new_position)
				if nextValue == 'Enemy':
					cost += abs(self.getEnemyAttack(new_position))
				elif nextValue == 'Food':
					cost -= abs(self.getFoodEnergy(new_position))
				elif nextValue == 'Wall':
					cost = 1000
				elif nextValue == 'Empty':
					pass

				value[i] = (new_position, cost)

			positions_dict[key] = value

		return positions_dict

# world={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (1,1): 2, (2,1):-3, (5,1): 0, (0,2):0, (5,2): 0, (0,3):0, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0 , (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}
# print 'test 1: object instantiation'
# m=Map(world)
# print m.world == {(3, 0): 0, (2, 1): -3, (5, 1): 0, (2, 5): 0, (0, 3): 0, (4, 0): 0, (5, 5): 0, (1, 5): 0, (5, 0): 0, (0, 4): 0, (5, 3): 0, (1, 1): 2, (5, 4):0,(0,0):0,(4,5):'x',(0,5):0,(1,0):0,(3,5):0,(0, 1): 0, (2, 0): 0, (5, 2): 0, (0, 2): 0}

# print 'test 2: whatIsAt'
# print m.whatIsAt((1,0))
# print 'test 3: whatIsAt'
# print m.whatIsAt((2,1))
# print 'test 4: whatIsAt'
# print m.whatIsAt((1,1))

# print 'test 5: getFoodEnergy'
# w1=m.getFoodEnergy((1,1))
# w2=m.getFoodEnergy((3,3))
# print (w1,w2)

# print 'test 6: getEnemyAttack'
# w1=m.getEnemyAttack((2,1))
# w2=m.getEnemyAttack((3,3))
# print (w1,w2)

# print 'test 7: removeEnemy'
# w1=m.getEnemyAttack((2,1))
# w2=m.removeEnemy((2,1))
# w3=m.getEnemyAttack((2,1))
# print (w1,w2,w3)

# print 'test 8: whatIsAt'
# print m.whatIsAt((1,4))
# print 'test 9: getFoodEnergy'
# print m.getFoodEnergy((1,4))
# print 'test 10: getEnemyAttack'
# print m.getEnemyAttack((1,4))
# print 'test 11: whatIsAt'
# print m.whatIsAt((4,5))
# print 'test 12: getExitPosition'
# print m.getExitPosition()
# print 'test 13: eatFood'
# w1=m.whatIsAt((1,1))
# w2=m.eatFood((1,1))
# w3=m.whatIsAt((1,1))
# print (w1,w2,w3)
# print 'test 14: test aliasing'
# print m.world == world

# world={(0,0):0, (1,0):0 , (2,0):0, (0,1):0, (1,1):-2, (2,1): 0, (0,2):0, (1,2): 'x', (2,2): 0}
# print 'test 1'
# m=Map(world)
# print m.getSearchMap() == {(0, 1): {0: ((0, 0), 1000), 1: ((1, 1), 2), 2: ((0, 2), 1000)}, (1, 2): {0: ((1, 1), 2), 1: ((2, 2), 1000), 3: ((0, 2), 1000)}, (0, 0): {1: ((1, 0), 1000), 2: ((0, 1), 1000)}, (2, 1): {0: ((2, 0), 1000), 2: ((2, 2), 1000), 3: ((1, 1), 2)}, (1, 1): {0: ((1, 0), 1000), 1: ((2, 1), 1000), 2: ((1, 2), 0), 3: ((0, 1), 1000)}, (2, 0): {2: ((2, 1), 1000), 3: ((1, 0), 1000)}, (2, 2): {0: ((2, 1), 1000), 3: ((1, 2), 0)}, (1, 0): {1: ((2, 0), 1000), 2: ((1, 1), 2), 3: ((0, 0), 1000)}, (0, 2): {0: ((0, 1), 1000), 1: ((1, 2), 0)}}

# world={(0,0):0, (1,0):0 , (2,0):0, (0,1):0, (1,1):3, (2,1): 0, (0,2):0, (1,2): 'x', (2,2): 0}
# print 'test 2'
# m=Map(world)
# print m.getSearchMap() == {(0, 1): {0: ((0, 0), 1000), 1: ((1, 1), 0), 2: ((0, 2), 1000)}, (1, 2): {0: ((1, 1), 0), 1: ((2, 2), 1000), 3: ((0, 2), 1000)}, (0, 0): {1: ((1, 0), 1000), 2: ((0, 1), 1000)}, (2, 1): {0: ((2, 0), 1000), 2: ((2, 2), 1000), 3: ((1, 1), 0)}, (1, 1): {0: ((1, 0), 1000), 1: ((2, 1), 1000), 2: ((1, 2), 3), 3: ((0, 1), 1000)}, (2, 0): {2: ((2, 1), 1000), 3: ((1, 0), 1000)}, (2, 2): {0: ((2, 1), 1000), 3: ((1, 2), 3)}, (1, 0): {1: ((2, 0), 1000), 2: ((1, 1), 0), 3: ((0, 0), 1000)}, (0, 2): {0: ((0, 1), 1000), 1: ((1, 2), 3)}}


# world={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2): -2, (5,2): 0, (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0 , (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}
# print 'test 3'
# m=Map(world)
# print m.getSearchMap() == {(1, 3): {0: ((1, 2), 5), 1: ((2, 3), 0), 2: ((1, 4), 3), 3: ((0, 3), 1000)}, (3, 0): {1: ((4, 0), 1000), 2: ((3, 1), 3), 3: ((2, 0), 1000)}, (5, 4): {0: ((5, 3), 1000), 2: ((5, 5), 1000), 3: ((4, 4), 3)}, (2, 1): {0: ((2, 0), 1000), 1: ((3, 1), 3), 2: ((2, 2), 3), 3: ((1, 1), 3)}, (5, 1): {0: ((5, 0), 1000), 2: ((5, 2), 1000), 3: ((4, 1), 3)}, (2, 5): {0: ((2, 4), 3), 1: ((3, 5), 1000), 3: ((1, 5), 1000)}, (0, 3): {0: ((0, 2), 1000), 1: ((1, 3), 3), 2: ((0, 4), 1000)}, (4, 0): {1: ((5, 0), 1000), 2: ((4, 1), 3), 3: ((3, 0), 1000)}, (1, 2): {0: ((1, 1), 3), 1: ((2, 2), 3), 2: ((1, 3), 3), 3: ((0, 2), 1000)}, (3, 3): {0: ((3, 2), 3), 1: ((4, 3), 3), 2: ((3, 4), 3), 3: ((2, 3), 0)}, (4, 4): {0: ((4, 3), 3), 1: ((5, 4), 1000), 2: ((4, 5), 3), 3: ((3, 4), 3)}, (1, 5): {0: ((1, 4), 3), 1: ((2, 5), 1000), 3: ((0, 5), 1000)}, (5, 0): {2: ((5, 1), 1000), 3: ((4, 0), 1000)}, (2, 2): {0: ((2, 1), 3), 1: ((3, 2), 3), 2: ((2, 3), 0), 3: ((1, 2), 5)}, (5, 3): {0: ((5, 2), 1000), 2: ((5, 4), 1000), 3: ((4, 3), 3)}, (4, 1): {0: ((4, 0), 1000), 1: ((5, 1), 1000), 2: ((4, 2), 3), 3: ((3, 1), 3)}, (1, 1): {0: ((1, 0), 1000), 1: ((2, 1), 3), 2: ((1, 2), 5), 3: ((0, 1), 1000)}, (3, 2): {0: ((3, 1), 3), 1: ((4, 2), 3), 2: ((3, 3), 3), 3: ((2, 2), 3)}, (0, 0): {1: ((1, 0), 1000), 2: ((0, 1), 1000)}, (4, 5): {0: ((4, 4), 3), 1: ((5, 5), 1000), 3: ((3, 5), 1000)}, (0, 4): {0: ((0, 3), 1000), 1: ((1, 4), 3), 2: ((0, 5), 1000)}, (5, 5): {0: ((5, 4), 1000), 3: ((4, 5), 3)}, (1, 4): {0: ((1, 3), 3), 1: ((2, 4), 3), 2: ((1, 5), 1000), 3: ((0, 4), 1000)}, (0, 5): {0: ((0, 4), 1000), 1: ((1, 5), 1000)}, (4, 2): {0: ((4, 1), 3), 1: ((5, 2), 1000), 2: ((4, 3), 3), 3: ((3, 2), 3)}, (1, 0): {1: ((2, 0), 1000), 2: ((1, 1), 3), 3: ((0, 0), 1000)}, (3, 5): {0: ((3, 4), 3), 1: ((4, 5), 3), 3: ((2, 5), 1000)}, (0, 1): {0: ((0, 0), 1000), 1: ((1, 1), 3), 2: ((0, 2), 1000)}, (5, 2): {0: ((5, 1), 1000), 2: ((5, 3), 1000), 3: ((4, 2), 3)}, (3, 1): {0: ((3, 0), 1000), 1: ((4, 1), 3), 2: ((3, 2), 3), 3: ((2, 1), 3)}, (0, 2): {0: ((0, 1), 1000), 1: ((1, 2), 5), 2: ((0, 3), 1000)}, (2, 0): {1: ((3, 0), 1000), 2: ((2, 1), 3), 3: ((1, 0), 1000)}, (4, 3): {0: ((4, 2), 3), 1: ((5, 3), 1000), 2: ((4, 4), 3), 3: ((3, 3), 3)}, (2, 3): {0: ((2, 2), 3), 1: ((3, 3), 3), 2: ((2, 4), 3), 3: ((1, 3), 3)}, (3, 4): {0: ((3, 3), 3), 1: ((4, 4), 3), 2: ((3, 5), 1000), 3: ((2, 4), 3)}, (2, 4): {0: ((2, 3), 0), 1: ((3, 4), 3), 2: ((2, 5), 1000), 3: ((1, 4), 3)}}
