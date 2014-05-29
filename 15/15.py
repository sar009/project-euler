import time
start_time = time.time()

class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

tree = []
size = 6 + 1
for x in range(size):
	tree.append([])
	for y in range(size):
		tree[x].append(Tree())

for x in range(size):
	for y in range(size):
		if y+1 < size:
			tree[x][y].right = tree[x][y+1]
		else:
			tree[x][y].right = None
		if x+1 < size:
			tree[x][y].left = tree[x+1][y]
		else:
			tree[x][y].left = None
		tree[x][y].data = x,y

done = False
trav_x = trav_y = 0
trace = []
count = 0
goleft = False

while not done:
	if tree[trav_x][trav_y].right and not goleft:
		trace.append((tree[trav_x][trav_y].data, 'R'))
		trav_y += 1
		continue
	elif tree[trav_x][trav_y].left:
		trace.append((tree[trav_x][trav_y].data, 'L'))
		if trace[0][1] == 'L':
			break
		trav_x += 1
		goleft = False
		continue
	elif tree[trav_x][trav_y].data == (size-1, size-1):
		count += 1
		# print count
		for i in range(len(trace)):
			if trace[len(trace)-i-1][1] == 'R':
				trace[len(trace)-i-1]
				if tree[trace[len(trace)-i-1][0][0]][trace[len(trace)-i-1][0][1]].left:
					trav_x = trace[len(trace)-i-1][0][0]
					trav_y = trace[len(trace)-i-1][0][1]
					trace = trace[:len(trace)-i-1]
					goleft = True
					break
		if not goleft:
			done = True
print count*2
print "calculate in ", time.time() - start_time, " seconds"