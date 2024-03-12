# Number of lines per View - this is assumed to be the view
# that you get from using an atlas or from being in the air.
# You get a smaller-sized ASCII map if you're on the ground.

VIEW_LINES = 15

# Row and column dimensions of the world. The way that I
# derived these values is discussed in README.md.

WORLD_ROWS = 1299
WORLD_COLS = 1995

#WORLD_ROWS = 99
#WORLD_COLS = 95

# The directory that logfiles are read from. You probably
# shouldn't set this to your normal everyday logfile directory.
#
# If you were experimenting and you have logs that are matching Views
# up to the wrong coordinates, that will affect the final map!
#
# Ideally, this directory is where you put vetted logfiles of atlas
# sessions that you produced *carefully*, with polished scripts,
# accurate coordinates, and possibly even extra safeguards like
# being chann deaf.

LOGDIR = "./logfiles/"

# Output file for the final map.

OUTFILE = "./wilderness.txt"

# I know this is super gross, but I couldn't figure out how to describe
# the pattern of visible points more elegantly - since the shape of the
# wilderness view has never changed and probably never will, this
# probably doesn't need to be refactored except for maybe OCD's sake

VISIBLE_POINTS = (
    [0,7],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[2,3],[2,4],[2,5],
    [2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[3,2],[3,3],[3,4],[3,5],[3,6],
    [3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[4,1],[4,2],[4,3],[4,4],[4,5],
    [4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[4,13],[5,1],[5,2],[5,3],
    [5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[6,1],
    [6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],
    [6,13],[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],
    [7,10],[7,11],[7,12],[7,13],[7,14],[8,1],[8,2],[8,3],[8,4],[8,5],
    [8,6],[8,7],[8,8],[8,9],[8,10],[8,11],[8,12],[8,13],[9,1],[9,2],[9,3],
    [9,4],[9,5],[9,6],[9,7],[9,8],[9,9],[9,10],[9,11],[9,12],[9,13],[10,1],
    [10,2],[10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],
    [10,11],[10,12],[10,13],[11,2],[11,3],[11,4],[11,5],[11,6],[11,7],
    [11,8],[11,9],[11,10],[11,11],[11,12],[12,3],[12,4],[12,5],[12,6],
    [12,7],[12,8],[12,9],[12,10],[12,11],[13,4],[13,5],[13,6],[13,7],
    [13,8],[13,9],[13,10],[14,7])