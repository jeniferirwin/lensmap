import os
import sys
from world import world

logfile = sys.argv[1]

def main() -> int:
    if not os.path.isfile(logfile):
        print("Could not find logfile: {}".format(logfile))
        sys.exit(1)

    with open(logfile) as file:
        log = file.readlines()
        if not len(log) > 15:
            print("Not a valid logfile: {}".format(logfile))

    map = world(1299, 1995)
    map.log_to_views(log)
    map.tidy_views()
    map.printmap()

if __name__ == '__main__':
    sys.exit(main())