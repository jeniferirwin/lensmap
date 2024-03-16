import os
import sys
from world import world
from config import *

def main() -> int:
    if not os.path.isdir(LOGDIR):
        print("Could not find log directory: {}".format(LOGDIR))
        return(1)

    loglines = []
    with os.scandir(LOGDIR) as logdir:
        for entry in logdir:
            with open(entry) as logfile:
                input_lines = logfile.readlines()
                loglines += input_lines

    print("Initializing world...")
    map = world(WORLD_ROWS, WORLD_COLS)
    print("Converting log to views...")
    map.log_to_views(loglines)
    print("Tidying views...")
    map.tidy_views()
    print("Plotting the points...")
    map.plot_points()
    print("Dumping the map...")
    #map.printmap()
    return(0)

if __name__ == '__main__':
    sys.exit(main())