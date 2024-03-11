# Number of lines per View - this is assumed to be the view
# that you get from using an atlas or from being in the air.
# You get a smaller-sized ASCII map if you're on the ground.

VIEW_LINES = 15

# Row and column dimensions of the world. The way that I
# derived these values is discussed in README.md.

WORLD_ROWS = 1299
WORLD_COLS = 1995

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