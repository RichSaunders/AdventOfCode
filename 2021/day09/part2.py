import numpy
import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()
    input = [list(map(int, x)) for x in input]
    floor = np.array(input)

basins = np.zeros(floor.shape, numpy.int16)
next_basin = 1

for y in range(floor.shape[1]):
    for x in range(floor.shape[0]):
        if floor[x,y] != 9:
            my_basin = basins[x, y]

            if x < floor.shape[0]-1:
                if basins[x+1, y] != 0:
                    # Tile to the right already has a basin set
                    if my_basin == 0:
                        # Copy it
                        my_basin = basins[x+1, y]
                        basins[x, y] = my_basin
                    else:
                        # Accidentally created an extra basin, merge them
                        basins[basins==basins[x+1, y]] = my_basin

                elif my_basin == 0:
                    # Tile is in a new basin
                    my_basin = next_basin
                    basins[x, y] = my_basin
                    next_basin += 1

                if floor[x+1, y] != 9:
                    # There isn't a peak to the right, so it's in the same basin as current tile
                    basins[x+1, y] = my_basin

            if y < floor.shape[1]-1:
                if floor[x, y+1] != 9:
                    # There isn't a peak below, so it's in the same basin as current tile
                    basins[x, y+1] = my_basin

basin_counts = numpy.unique(basins, return_counts=True)[1][1:]
basin_counts = sorted(basin_counts, reverse=True)

print(basin_counts[0] * basin_counts[1] * basin_counts[2])
