import time

start_time = time.time()

size = 20 + 1

latice_points = []
for i in range(size):
    latice_points.append(range(size))

for i in range(size):
    for j in range(size):
        if i == 0 or j == 0:
            latice_points[i][j] = 1
        else:
            latice_points[i][j] = latice_points[i - 1][j] + latice_points[i][j - 1]

print latice_points[size - 1][size - 1]
print "calculated in ", time.time() - start_time, " seconds"