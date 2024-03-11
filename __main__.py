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

    map = world(WORLD_ROWS, WORLD_COLS)
    map.log_to_views(loglines)
    map.tidy_views()
    map.plot_points()
    map.printmap()
    return(0)

if __name__ == '__main__':
    sys.exit(main())