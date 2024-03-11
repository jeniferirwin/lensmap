import re
from lensmoor.worldmap.view import room
from strings import *
from array import *

class world:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.views = []
        self.plot = [[' ']*self.cols for i in range(self.rows)]

    def coord_check(self, coords):
        if coords is not None:
            if self.current_view is not None:
                self.current_view.x = int(coords.group(1)) - 1
                self.current_view.y = int(coords.group(2)) - 1
                self.views.append(self.current_view)
            self.current_view = room()
            return True
        return False

    def log_to_views(self, log):
        """Turn a whole logfile into a series of views.
        """
        keysearch = 0
        for line in log:
            coords = re.search(RE_COORDS, line)
            if self.coord_check(coords):
                keysearch = room.ROOM_LINES
            if keysearch > 0 and coords is None:
                self.current_view.lines.append(line)
                keysearch -= 1
    
    def tidy_rooms(self):
        for view in self.views:
            view.remove_legend()
            view.replace_roads()
            view.remove_colors()
            view.remove_newlines()
    
    def is_coord_valid(self, x, y):
        if x >= 0 and x < self.cols and y >= 0 and y < self.rows:
            return True
        return False

    def printmap(self):
        for row in self.plot:
            newline = ''
            for col in row:
                newline += col
            print(newline)