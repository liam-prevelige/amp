# Grid Legend
# W = wall
# C = confinement
# P = patrolling
# S = safe zone
# D = door

X_OFFSET = 19.53 # The offset of the left of the map from center
Y_OFFSET = 13.97 # The offset of the top of the map from center
# NUM_ROWS = 55 # Number of rows in the grid
# NUM_COLS = 77 # Number of columns in the grid
NUM_ROWS = 165 # Number of rows in the grid
NUM_COLS = 231 # Number of columns in the grid
MAP_HEIGHT = 27.94 # Height of the map
MAP_WIDTH = 39.06 # Width of the map
ROW_PER_Y = NUM_ROWS / MAP_HEIGHT # Number of rows per unit Y
COL_PER_X = NUM_COLS / MAP_WIDTH # Number of columns per unit X

# Adapted from https://github.com/mlyean/grid-pathfinding/blob/master/grid.py
class Grid(object):
	def __init__(self, path):
		"""Constructor"""
		self.grid = []

		with open(path, "r") as g_file: # Read grid from file
			lines = g_file.read().splitlines() # For each line
			for line in lines:
				line = line.replace(" ", "") # Remove the spaces
				self.grid.append(line.split(",")[:-1]) # Append each cell seperated by commas

		self.rows = len(self.grid) # Get number of rows
		self.cols = len(self.grid[0]) # Get number of columns

	def get_adjacent(self, node):
		"""Return the adjacent nodes of a given node"""
		y = node[0] # Vertical (Y) index of the node
		x = node[1] # Horizontal (X) index of the node

		if x < 0 or y < 0 or x > self.cols or y > self.rows: # If it's out of bounds
			return [] # Return empty

		if self.grid[y][x] == 'W': # If it's a wall
			return [] # Return empty
		
		adjacent = []
		for pos in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
			if 0 <= y + pos[0] < self.rows and 0 <= x + pos[1] < self.cols:
				if self.grid[y + pos[0]][x + pos[1]] != 'W':
					for next_pos1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
						if 0 <= y + pos[0] + next_pos1[0] < self.rows and 0 <= x + pos[1] + next_pos1[1] < self.cols:
							if self.grid[y + pos[0] + next_pos1[0]][x + pos[1] + next_pos1[1]] != 'W':
								for next_pos2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
									if 0 <= y + pos[0] + next_pos1[0] + next_pos2[0] < self.rows and 0 <= x + pos[1] + next_pos1[1] + next_pos2[1] < self.cols:
										if self.grid[y + pos[0] + next_pos1[0] + next_pos2[0]][x + pos[1] + next_pos1[1] + next_pos2[1]] != 'W':
											for next_pos3 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
												if 0 <= y + pos[0] + next_pos1[0] + next_pos2[0] + next_pos3[0] < self.rows and 0 <= x + pos[1] + next_pos1[1] + next_pos2[1] + next_pos3[1] < self.cols:
													if self.grid[y + pos[0] + next_pos1[0] + next_pos2[0] + next_pos3[0]][x + pos[1] + next_pos1[1] + next_pos2[1] + next_pos3[1]] != 'W':
														adjacent.append((y + pos[0], x + pos[1]))
													else:
														break
										else:
											break
							else:
								return []
				else:
					return []
							
		return adjacent # Return

	def get_nodes(self):
		"""Get all the nodes of the grid except for the walls"""
		nodes = []
		for i in range(self.rows): # For each row
			for j in range(self.cols): # For each column
				if self.grid[i][j] != 'W': # If it's not a wall
					nodes.append((i, j)) # Add it to the return list
		return nodes # Return

	def get_node_at(self, x, y):
		"""Get node corresponding to given coordinate"""
		return self.grid[int((-y + Y_OFFSET) * ROW_PER_Y)][int((x + X_OFFSET) * COL_PER_X)]

	def get_grid_value(self, x, y):
		"""Get the value of the node at given index"""
		return self.grid[x][y]

	def set_grid_value(self, r, c, val):
		"""Set the value of the node at given index"""
		self.grid[r][c] = val

	def get_num_rows(self):
		"""Get number of rows"""
		return self.rows

	def get_num_columns(self):
		"""Get number of columns"""
		return self.cols
	
	def get_grid_arr(self):
		return self.grid


def get_node_col(x):
	"""Get the column corresponding to X coordinate"""
	return int((x + X_OFFSET) * COL_PER_X)

def get_node_row(y):
	"""Get the row corresponding to Y coordinate"""
	return int((-y + Y_OFFSET) * ROW_PER_Y)

def get_node_x(col):
	"""Get the X coordinate of the given column"""
	return col / COL_PER_X - X_OFFSET

def get_node_y(row):
	"""Get the Y coordinate of the given row"""
	y = row / ROW_PER_Y
	return Y_OFFSET - y

def get_velocity_at(arr, x, y):
	"""Get the grid velocity at given location"""
	return arr[int((-y + Y_OFFSET) * ROW_PER_Y)][int((x + X_OFFSET) * COL_PER_X)]
