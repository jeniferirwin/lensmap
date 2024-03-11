from strings import *
import re

class view:
    VIEW_LINES = 15

    # I know this is super gross but I couldn't figure out how to describe
    # the pattern of visible points more elegantly - since the shape of the
    # wilderness view has never changed and probably never will, this probably
    # doesn't need to be refactored except for maybe OCD's sake

    VISIBLE = ([0,7],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[2,3],[2,4],
               [2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[3,2],[3,3],[3,4],
               [3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[4,1],[4,2],
               [4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],
               [4,13],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],
               [5,10],[5,11],[5,12],[5,13],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],
               [6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[6,13],[7,0],[7,1],[7,2],
               [7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],
               [7,13],[7,14],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8],
               [8,9],[8,10],[8,11],[8,12],[8,13],[9,1],[9,2],[9,3],[9,4],[9,5],
               [9,6],[9,7],[9,8],[9,9],[9,10],[9,11],[9,12],[9,13],[10,1],[10,2],
               [10,3],[10,4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],
               [10,12],[10,13],[11,2],[11,3],[11,4],[11,5],[11,6],[11,7],[11,8],
               [11,9],[11,10],[11,11],[11,12],[12,3],[12,4],[12,5],[12,6],[12,7],
               [12,8],[12,9],[12,10],[12,11],[13,4],[13,5],[13,6],[13,7],[13,8],
               [13,9],[13,10],[14,7])

    def __init__(self):
        self.lines = []
        self.x = 0
        self.y = 0

    def remove_colors(self):
        """Strip out all colors. Only run this AFTER running the
        `replace_roads` function, or roads and rivers will become
        identical in the final product!
        """
        colorless = []
        for line in self.lines:
            line = line.replace('\x1b[0m','')
            line = line.replace('\x1b[\d;3\dm','')
            colorless.append(line)
        self.lines = colorless
    
    def remove_legend(self):
        """Strip the key/legend out of the view."""
        keyless = []
        for line in self.lines:
            for string in LEGEND_STRINGS:
                line = line.replace(string, NEWLINE)
            keyless.append(line)
        self.lines = keyless
    
    def remove_newlines(self):
        """Tighten up the lines by removing excess spaces and newlines.
        Originally this was included as part of `remove_colors` but
        I decided to make it optional in case future forks have some
        need to preserve all spaces and newlines in each view.
        """
        trimmed = []
        for line in self.lines:
            line = re.sub(' *\n','',line)
            trimmed.append(line)
        self.lines = trimmed

    def replace_roads(self):
        """Replace all roads with numbers 1-5. See README.md for why
        we're doing this, but the gist of it is so that we can tell
        the difference between roads and rivers without color.
        
        I feel like all the magic strings here are nasty but that it
        might also be overkill to give them their own constants.
        """
        fixed = []
        for line in self.lines:
            line = line.replace('\x1b[1;37m+',"1")
            line = line.replace('\x1b[1;37m-',"2")
            line = line.replace('\x1b[1;37m|',"3")
            line = line.replace('\x1b[1;37m\\',"4")
            line = line.replace('\x1b[1;37m/',"5")
            match = re.search('([1-5])([\/+|-])',line)
            while match is not None:
                line = re.sub('([1-5])\+', '\g<1>1', line)
                line = re.sub('([1-5])\-', '\g<1>2', line)
                line = re.sub('([1-5])\|', '\g<1>3', line)
                line = re.sub('([1-5])\\\\', '\g<1>4', line)
                line = re.sub('([1-5])\/', '\g<1>5', line)
                match = re.search('([1-5])([\/+|-])',line)
            fixed.append(line)
        self.lines = fixed