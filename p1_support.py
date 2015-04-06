
# Support code for P1
# https://courses.soe.ucsc.edu/courses/cmpm146/Spring15/01

def load_level(filename):

	walls = {}
	spaces = {}
	waypoints = {}

	# terrain 
	water = {}
	sand = {}

	with open(filename, "r") as f:

		for j, line in enumerate(f.readlines()):
			for i, char in enumerate(line):
				if char == '\n':
					continue
					# if upper case which in this case X is the only upperCase Letter
				elif char.isupper() and char != 'W' and char != 'S':
					walls[(i,j)] = char
					# anything else is considered a space 
				else:
					if char != 'W' and char != 'S':
						spaces[(i,j)] = char
					# if the char is lower case then it will be a way point so a b c etc 
					if char == 'W':
						water[(i,j)] = char
					elif char == 'S':
						sand[(i,j)] = char
					elif char.islower():
						waypoints[char] = (i,j)

	# define level which will be used in main file 
	level = { 'walls': walls,
			  'spaces': spaces,
			  'water': water,
			  'sand': sand,
			  'waypoints': waypoints}

	return level

# display level that was read in from file with a path pointing to the 
# specified way points 
def show_level(level, path=[]):

	xs, ys = zip(*(level['spaces'].keys() + level['walls'].keys()))
	x_lo = min(xs)
	x_hi = max(xs)
	y_lo = min(ys)
	y_hi = max(ys)

	path_cells = set(path)

	chars = []

	for j in range(y_lo, y_hi+1):
		for i in range(x_lo, x_hi+1):

			cell = (i,j)
			if cell in path_cells:
				chars.append('*')
			elif cell in level['walls']:
				chars.append(level['walls'][cell])
			elif cell in level['water']:
				chars.append(level['water'][cell])
			elif cell in level['sand']:
				chars.append(level['sand'][cell])
			elif cell in level['spaces']:
				chars.append(level['spaces'][cell])
			else:
				chars.append(' ')
				
		chars.append('\n')

	print ''.join(chars)
