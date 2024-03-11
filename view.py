from strings import *
import re

class view:
    def __init__(self, x, y):
        self.lines = []
        self.x = int(x)
        self.y = int(y)

    def remove_colors(self):
        """Strip out all colors. Only run this AFTER running the
        `replace_roads` function, or roads and rivers will become
        identical in the final product!
        """
        colorless = []
        for line in self.lines:
            line = re.sub('\x1b\[0m','',line)
            line = re.sub('\x1b\[\d;3\dm','',line)
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