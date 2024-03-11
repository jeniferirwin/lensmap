import re
from view import view
from strings import *
from array import *
from config import *

class world:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.views = []
        self.plot = [[' ']*self.cols for i in range(self.rows)]

    def log_to_views(self, log):
        """Process input text into a series of views. To process the
        text efficiently and accurately, there are four stages.

        COORDINATE SEARCH

        By default, we check each line to see if it's a COORDINATES
        line. To see an example of this, see the 'Necessary Scripts'
        section of README.md.

        If we find coordinates at this stage, we start a new View
        and assign the new coordinates to it. If we don't find any
        coordinates, we just move on to the next line.

        KEY SEARCH

        After the Coordinates have been found, then we start to look
        for the 'key line'. Whenever you get the automap output from
        the MUD, the very first line of it also includes the top of
        the legend, where it says `-------KEY-------`.
        
        By searching for this string in particular, we'll know for
        sure that we've encountered the first line of a View, so we
        use this as an anchor point to start reading lines into the
        View object. At this point, we set the `lines_left` variable
        to VIEW_LINES - 1, since we're already reading in this first
        line.

        LINES_LEFT

        While `lines_left` is above 0, we just read in whatever line
        we've got without trying to match anything on it. With the
        way the MUD output works, it is impossible for the automap
        view to be broken up by other lines unless there is some
        sort of extreme malfunction in the client, so we can be
        reasonably certain that every line in this chunk is valid.

        NO LINES LEFT

        Once `lines_left` reaches 0, we commit the View to self.views 
        and start the process over again by setting `coords_searching`
        to True.
        """
        key_searching = False
        coords_searching = True
        lines_left = 0
        current_view = None

        for line in log:
            if coords_searching is True:
                coord_match = re.search(RE_COORDS,line)
                if coord_match is not None:
                    current_view = view(coord_match.group(1), coord_match.group(2))
                    key_searching = True
                    coords_searching = False
                continue

            if key_searching is True:
                ansi_search = re.search(KEY_STRING_ANSI,line)
                flat_search = re.search(KEY_STRING,line)
                if ansi_search is not None or flat_search is not None:
                    current_view.lines.append(line)
                    lines_left = VIEW_LINES - 1
                    key_searching = False
                continue

            if lines_left > 0:
                current_view.lines.append(line)
                lines_left -= 1
                continue

            if lines_left == 0:
                coords_searching = True
                if current_view is not None:
                    self.views.append(current_view)
                
    def tidy_views(self):
        """Run all the tidying commands on the lines in the views.
        Do not change the order of these unless you've made changes
        that require it.
        """
        for view in self.views:
            view.remove_legend()
            view.replace_roads()
            view.remove_colors()
    
    def printmap(self):
        maplines = []
        for row in self.plot:
            newline = ''
            for col in row:
                newline += col
            maplines.append(newline + '\n')
        outfile = open(OUTFILE, "w")
        outfile.writelines(maplines)
        outfile.close()