# World Class
#
# Stores the map in a useful way,
# keeps track of cell info, loads
# new maps from files, and answers
# questions about the map.
#
# 2014/3/21
# written by Michael Shawn Redmond

from config import *
import rectangle
import pygame
import os

class World:
    def __init__(self, position, width, height, layout_file=None):
        self.position = position
        self.width = self.safe_assign("Width", width, int, WORLD_DEFAULT_WIDTH)
        self.height = self.safe_assign("Height", height, int, WORLD_DEFAULT_HEIGHT)
        self.cell_width = TILE_WIDTH
        self.cell_height = TILE_HEIGHT
        self.layout = []
        if layout_file is not None:
            self.load_from_file(layout_file)
            
    # attempts to assign a variable called var_name (for debugging)
    # to a value of value but assigns it to value: default
    # if the original type cannot be casted into desired_type
    def safe_assign(self, var_name, value, desired_type, default):
        if type(desired_type) != type(type(int)):
            print "Desired_type was not a valid type"
            print "Defaulting to type(str)"
            desired_type = str
        if type(value) != desired_type:
            print str(var_name) + " expected to be " + str(desired_type)
            print "Attempting Cast..."
            try:
                value = desired_type(value)
            except:
                print "Unable to convert ", type(value), " to type " + str(desired_type)
                print "Defaulting to", default
                value = default
            print "Type-cast completed"
        return value

    # attempts to open the world file and store the information
    # does nothing if the file was invalid in any way
    def load_from_file(self, layout_file):
        if not os.path.exists(layout_file):
            print "Error loading world file " + layout_file + ": File was not found."
            print "File will not be loaded"
            return
        f = open(layout_file, 'rb')
        fin = [line.strip() for line in f.readlines()]
        f.close()
        dim = fin[0].split()
        try:
            dim[0] = int(dim[0])
            dim[1] = int(dim[1])
            if len(dim) != 2:
                raise Exception("Invalid dimension description\n" + str(dim))
            layout = []
            fin = fin[1:]
            for line in fin:
                if len(line) != dim[0]:
                    raise Exception("Invalid/Mismatched width\n" + str(line))
                else:
                    layout.append(line)
            if len(layout) != dim[1]:
                l = ""
                for i in layout:
                    l += i + '\n'
                l = l.strip()
                raise Exception("Invalid/Mismatched height\n" + l)
        except Exception, e:
            print "Error loading world file " + layout_file + ": Invalid formatting"
            print e
            return False
        row_size = self.width/self.cell_width
        col_size = self.height/self.cell_height
        filled_rows = int(dim[0])
        filled_cols = int(dim[1])
        empty_rows = row_size - filled_rows
        empty_cols = col_size - filled_cols
        for i in range(len(layout)):
            fill = empty_rows*'0'
            layout[i] = layout[i] + fill
        for i in range(empty_cols):
            fill = row_size*'0'
            layout.append(fill)
        self.layout = []
        for j in range(len(layout)):
            r = []
            for i in range(len(layout[j])):
                tile = layout[j][i]
                if tile == '0':
                    img = pygame.image.load(GRASS_IMG)
                else:
                    img = pygame.image.load(PATH_IMG)
                x = self.position[0] + (i)*self.cell_width
                y = self.position[1] + (j)*self.cell_height
                r.append(rectangle.Rectangle((x, y), img, self.cell_width, self.cell_height))
            self.layout.append(r)
        return True

    def paint(self, surface):
        for row in self.layout:
            for cell in row:
                cell.paint(surface)

    def __str__(self):
        board = ""
        for row in self.layout:
            line = ""
            for cell in row:
                line += str(cell)
            board += line + '\n'
        return board
