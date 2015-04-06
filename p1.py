from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop


def dijkstras_shortest_path(src, dst, graph, adj):
	"""Find a path from the source to target on the graph using Dijkstra shortest path algorithim """

	# intialize structures
	dist = {}
	prev = {}
	queve = []
	dist[src] = 0
	prev[src] = None
	heappush(queve,(dist[src],src))



	# while queve is not empty 
	while queve:
		#returns distance and node 
		bdist,node = heappop(queve)
	 	# if node has reached its destination cell it will quit while loop
		if node == dst:
			break
		# calls the get_steps function stored in adj
		neighbors = adj(graph, node)
		for v in neighbors:
			alt = bdist + length(graph,v,node)
			if v not in dist or alt < dist[v]:
				dist[v] = alt
				prev[v] = node
				heappush(queve,(dist[v],v))

	# if node is equal to the specified destination node dst
	if node == dst:
		path = []
		# while node is not empty 
		while node:
			path.append(node)
			node = prev[node]
		path.reverse()
		return path
	else:
		# returns an empty path because path from src to dst is not possible 
		return []

def length(level,cellA,cellB):
	xA,yA = cellA
	xB,yB = cellB

	# keeps track of terrain changes 
	t = 1

	# if one of the cells contains a water path then the cost to go through
	# that path increases by 6
	if cellA in level['water']:
		t = 6
	if cellA in level['sand']:
		t = 3
	return (sqrt(pow((xB - xA),2) + pow((yB - yA),2)))*t

# checks if the cell is a wall,space and water. Returns valid neighbors
# which are water and spaces 
def navigation_edges(level, cell):
	steps = []
	x, y = cell
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			dist = sqrt(dx*dx+dy*dy)
			if dist > 0 and next_cell in level['spaces']:
				steps.append(next_cell)
			elif dist > 0 and next_cell in level['water']:
				steps.append(next_cell)
			elif dist > 0 and next_cell in level['sand']:
				steps.append(next_cell)
	return steps


def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)